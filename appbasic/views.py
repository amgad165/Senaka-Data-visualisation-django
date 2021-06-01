# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect, JsonResponse
from django.db import connections
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
import requests
import json
from braces.views import LoginRequiredMixin
from django.views import generic
from django.db.models import Q
from appbasic.models import Account
from appbasic.utilities import SumForPieChart,SumForBarChart,ProgressChart,progress_percentage,list_of_all_lists,on_time,date_by_sub_business_days,working_days
import MySQLdb
import pandas as pd
import datetime
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from appbasic.models import Settings,Exceptions,date_range
from appbasic.models import Settings as settings_model



class DeleteException(DeleteView):
    model = Exceptions
    success_url = '/select_exceptions/'

class UpdateException(UpdateView):
    model = Exceptions
    success_url = '/select_exceptions/'
    fields = '__all__'

class CreateException(CreateView):
    model = Exceptions
    success_url = '/select_exceptions/'
    fields = '__all__'

class ExceptionLIST(ListView):
    model = Exceptions
    context_object_name = 'exceptions_list'

class UpdateSettings(UpdateView):
    model = Settings
    fields = '__all__'
    success_url = '/'

class Settings(CreateView):
    model = Settings
    fields = '__all__'
    success_url = '/'


@login_required
def company_color(request):
    daterange_objects= date_range.objects.all()
    if request.method == "POST":
        date=request.POST['daterange']
        date=date.split('–')
        if len(date)==2:
            date[1]=date[1][1:]
            if daterange_objects :
                print("not empty")
                object=daterange_objects[0]
                object.start_date=date[0]
                object.end_date=date[1]
                object.save()

            else:
                print("empty")
                object = date_range(start_date=date[0], end_date=date[1])
                object.save()

    conn = MySQLdb.connect(host = "213.190.6.85", user = "u370015874_test", passwd = "Test1234", db = "u370015874_test")
    query = "select * from ordersummary;"
    df_ordersummary = pd.read_sql(query,conn)

    query = "select ORDER_NUMBER,USER_NAME,WINDOWS_QTY,LINE_QTY,OPENING_QTY,ORDER_DATE from windowsentry;"
    df_windowsentry = pd.read_sql(query,conn)
    # window entry for monthly forecast

    df_windowsentry['WINDOWS_QTY'] = pd.to_numeric(df_windowsentry['WINDOWS_QTY'])
    df_windowsentry['LINE_QTY'] = pd.to_numeric(df_windowsentry['LINE_QTY'])
    df_windowsentry['OPENING_QTY'] = pd.to_numeric(df_windowsentry['OPENING_QTY'])
    df_windowsentry['ORDER_DATE'] = pd.to_datetime(df_windowsentry['ORDER_DATE'])

    if daterange_objects:

        start_date =pd.to_datetime(daterange_objects[0].start_date)
        end_date =pd.to_datetime(daterange_objects[0].end_date)
        # range for df_windowsentry
        mask = (df_windowsentry['ORDER_DATE'] >= start_date) & (df_windowsentry['ORDER_DATE'] <= end_date)
        df_windowsentry = df_windowsentry.loc[mask]



    Total_WINDOWSIN  = df_windowsentry['OPENING_QTY'].sum()
    Total_SINGLEWINDOWS  = df_windowsentry['WINDOWS_QTY'].sum()
    Total_WINDOWSEACHPRSON  = df_windowsentry['LINE_QTY'].sum()

    card_list=[Total_WINDOWSIN,Total_SINGLEWINDOWS]
# ----------------------------------------------------------------


# COMPANY
    company_total=[]
    company_names=[]
    company_total_sec=[]
    company_names_sec=[]


    order_summary_comapany=df_ordersummary['COMPANY'].unique()
    for company in  order_summary_comapany:
        sum_windowqty = 0
        orders = df_ordersummary.loc[df_ordersummary['COMPANY'] == company,'ORDER#']
        for order in orders:
            if order in df_windowsentry['ORDER_NUMBER'].values:
                windowqty=df_windowsentry.loc[df_windowsentry['ORDER_NUMBER'] == order,'WINDOWS_QTY'].iloc[0]
                sum_windowqty += windowqty

        company_total.append(sum_windowqty)
        company_names.append(company)
    if len(company_total)> 0:
        company_total, company_names = (list(t) for t in zip(*sorted(zip(company_total, company_names),reverse=True)))


#second column for COMPANY
    i=0
    while i < len(company_names):
        if company_total[i]== 0:
            company_total_sec.append(company_total[i])
            company_names_sec.append(company_names[i])
        i += 1

#third column for COMPANY
# dare range forecast
    df_windowsentry_forecast=df_windowsentry
    df_windowsentry_forecast = df_windowsentry_forecast.sort_values(by="ORDER_DATE" , ascending=False)
    forecast_dates=[]
    forecast_total=[]
    for date in  df_windowsentry_forecast['ORDER_DATE'].unique():
        df_sum_windowqty=df_windowsentry_forecast.loc[df_windowsentry_forecast['ORDER_DATE'] == date,'WINDOWS_QTY']
        total_forecast_windowqty=df_sum_windowqty.values.sum()
        date=pd.to_datetime(str(date))
        date=date.strftime("%d,%B %Y")
        forecast_dates.append(date)
        forecast_total.append(total_forecast_windowqty)


    company_data=[company_names,company_total,company_names_sec,company_total_sec,forecast_dates,forecast_total]

    daterange= date_range.objects.all()
    if daterange:
        daterange=daterange[0]
    conn.close()
    return render(request,"color_tracking/company_color.html",{"company_data":company_data,"daterange":daterange,"card_list":card_list})

@login_required
def new_orders(request):
    daterange_objects= date_range.objects.all()
    if request.method == "POST":
        date=request.POST['daterange']
        date=date.split('–')
        if len(date)==2:
            date[1]=date[1][1:]
            if daterange_objects :
                print("not empty")
                object=daterange_objects[0]
                daterange=daterange_objects[0]
                object.start_date=date[0]
                object.end_date=date[1]
                object.save()

            else:
                print("empty")
                object = date_range(start_date=date[0], end_date=date[1])
                object.save()

    conn = MySQLdb.connect(host = "213.190.6.85", user = "u370015874_test", passwd = "Test1234", db = "u370015874_test")
    query = "select * from ordersummary;"
    df_ordersummary = pd.read_sql(query,conn)

    query = "select ORDER_NUMBER,USER_NAME,WINDOWS_QTY,LINE_QTY,OPENING_QTY,ORDER_DATE from windowsentry;"
    df_windowsentry = pd.read_sql(query,conn)
    # window entry for monthly forecast

    df_windowsentry['WINDOWS_QTY'] = pd.to_numeric(df_windowsentry['WINDOWS_QTY'])
    df_windowsentry['LINE_QTY'] = pd.to_numeric(df_windowsentry['LINE_QTY'])
    df_windowsentry['OPENING_QTY'] = pd.to_numeric(df_windowsentry['OPENING_QTY'])
    df_windowsentry['ORDER_DATE'] = pd.to_datetime(df_windowsentry['ORDER_DATE'])


    df_windowsentry_forecast=df_windowsentry

    query = "select USER_NAME,WINDOWS_QTY,LINE_QTY,OPENING_QTY,ORDER_DATE from quotaiontoorder;"
    df_quotaiontorder = pd.read_sql(query,conn)
    df_quotaiontorder['ORDER_DATE'] = pd.to_datetime(df_quotaiontorder['ORDER_DATE'])

    if daterange_objects:


        start_date =pd.to_datetime(daterange_objects[0].start_date)
        end_date =pd.to_datetime(daterange_objects[0].end_date)
        # range for df_windowsentry
        mask = (df_windowsentry['ORDER_DATE'] >= start_date) & (df_windowsentry['ORDER_DATE'] <= end_date)
        df_windowsentry = df_windowsentry.loc[mask]

        # range for df_quotaiontorder
        mask = (df_quotaiontorder['ORDER_DATE'] >= start_date) & (df_quotaiontorder['ORDER_DATE'] <= end_date)
        df_quotaiontorder = df_quotaiontorder.loc[mask]







    Total_WINDOWSIN  = df_windowsentry['OPENING_QTY'].sum()
    Total_SINGLEWINDOWS  = df_windowsentry['WINDOWS_QTY'].sum()
    Total_WINDOWSEACHPRSON  = df_windowsentry['LINE_QTY'].sum()
    card_list=[Total_WINDOWSIN,Total_SINGLEWINDOWS]
# ----------------------------------------------------------------
#  WINDOW ENTRY
    unique_usernames=df_windowsentry.USER_NAME.unique()
    pie_windowsentry_username=[]
    pie_windowsentry_count=[]

    for username in unique_usernames:
        df_username_lineqty=df_windowsentry.loc[df_windowsentry['USER_NAME'] == username,'LINE_QTY']
        Total_WINDOWSEACHPRSON  = df_username_lineqty.values.sum()
        pie_windowsentry_username.append(username)
        pie_windowsentry_count.append(Total_WINDOWSEACHPRSON)

#  quotaiontorder
    unique_usernames=df_quotaiontorder.USER_NAME.unique()
    df_quotaiontorder['Count_Column'] = df_quotaiontorder['USER_NAME'].map(df_quotaiontorder['USER_NAME'].value_counts())
    pie_quotaiontorder_username=[]
    pie_quotaiontorder_count=[]

    for username in unique_usernames:
        count_of_username=df_quotaiontorder.loc[df_quotaiontorder['USER_NAME'] == username,'Count_Column'].iloc[0]
        pie_quotaiontorder_username.append(username)
        pie_quotaiontorder_count.append(count_of_username)




# monthly forecast
    df_windowsentry_forecast = df_windowsentry_forecast.sort_values(by="ORDER_DATE" , ascending=False)
    yesterday =pd.to_datetime(datetime.date.today() - datetime.timedelta(days=1))
    last_month =pd.to_datetime(yesterday - datetime.timedelta(days=30))
    mask = (df_windowsentry_forecast['ORDER_DATE'] >= last_month) & (df_windowsentry_forecast['ORDER_DATE'] <= yesterday)
    df_windowsentry_forecast = df_windowsentry_forecast.loc[mask]
    forecast_dates=[]
    forecast_total=[]
    for date in  df_windowsentry_forecast['ORDER_DATE'].unique():
        df_sum_windowqty=df_windowsentry_forecast.loc[df_windowsentry_forecast['ORDER_DATE'] == date,'WINDOWS_QTY']
        total_forecast_windowqty=df_sum_windowqty.values.sum()
        date=pd.to_datetime(str(date))
        date=date.strftime("%d,%B %Y")
        forecast_dates.append(date)
        forecast_total.append(total_forecast_windowqty)
    if len(pie_windowsentry_count)>0:
        pie_windowsentry_count, pie_windowsentry_username = (list(t) for t in zip(*sorted(zip(pie_windowsentry_count, pie_windowsentry_username),reverse=True)))
    if len(pie_quotaiontorder_count)>0 :
        pie_quotaiontorder_count, pie_quotaiontorder_username = (list(t) for t in zip(*sorted(zip(pie_quotaiontorder_count, pie_quotaiontorder_username))))

    pie_windowsentry_total=sum(pie_windowsentry_count)
    print(pie_windowsentry_total)
    pie_windowsentry_count_perc=[]
    for element in pie_windowsentry_count:
        pie_windowsentry_count_perc.append(round((element/pie_windowsentry_total)*100,1))

    data_list=[pie_windowsentry_username,pie_windowsentry_count,pie_quotaiontorder_username,pie_quotaiontorder_count,forecast_dates,forecast_total,pie_windowsentry_count_perc]
    conn.close()
    daterange= date_range.objects.all()
    if daterange:
        daterange=daterange[0]
    return render(request,"color_tracking/new_orders.html",{"data_list":data_list,"daterange":daterange,"card_list":card_list})

@login_required
def express_coating(request):
    print("1")
    conn = MySQLdb.connect(host = "213.190.6.85", user = "u370015874_test", passwd = "Test1234", db = "u370015874_test")
    try:
        print("2")


        # -----Settings------
        setting_object= settings_model.objects.all()
        if setting_object :
            setting_object=setting_object[0]


        # ________Dataframe part__________
        query = "select * from ordersummary;"
        df = pd.read_sql(query,conn,columns=['ORDER#','LIST DATE'])
        df=df[df['LIST DATE']!='']
        df=df[(df['COLOUR IN']!='WHT') | (df['COLOUR OUT']!='WHT')]

        df = df.sort_values(by="LIST DATE")
        df['LIST DATE'] = pd.to_datetime(df['LIST DATE'])
        Current_Date =pd.to_datetime(datetime.date.today())

        Nextweek_Date =pd.to_datetime(datetime.date.today() + datetime.timedelta(days=setting_object.loading_days))
        mask = (df['LIST DATE'] >= Current_Date) & (df['LIST DATE'] <= Nextweek_Date)
        df = df.loc[mask]
        print("5")
        # ------ table framecutting ----
        query = "select F,J,U,H,L from framescutting;"
        df_framescutting = pd.read_sql(query,conn)
        df_framescutting['U'] = pd.to_datetime(df_framescutting['U'])


        #count orders using exceptions
        exceptions_model =Exceptions.objects.all()
        if exceptions_model:
            for exception in exceptions_model :
                if exception.urban_part != None and exception.window_type != None:
                    print("both")
                    df_framescutting = df_framescutting[~(df_framescutting['H'] == exception.urban_part) | (df_framescutting['L'] == exception.window_type)]


                elif exception.window_type == None :
                    print("window_type empty")
                    df_framescutting = df_framescutting[(df_framescutting['H'] != exception.urban_part)]

                elif exception.urban_part == None :
                    print("urban_part empty")
                    df_framescutting = df_framescutting[(df_framescutting['L'] != exception.window_type)]


        df_framescutting['Count_Column'] = df_framescutting['J'].map(df_framescutting['J'].value_counts())
        print("6")

        # ----- table FrameClearing ---
        query = "select Id,Date from FrameClearing;"
        print("7")
        df_frameclearing = pd.read_sql(query,conn)

        query = "select Id,Date from ColourShipping;"
        df_ColourShipping = pd.read_sql(query,conn)

        query = "select Id,Date,Line from ExpressCoatingColorReceiving;"
        df_ExpressCoatingColourReceiving = pd.read_sql(query,conn)

        # query = "select Id,Date,Line from DVCoatexColorReceiving;"
        # df_DVCoartingColourReceiving = pd.read_sql(query,conn)

        query = "select Id,Date from ColourReceiving;"
        df_vp_received = pd.read_sql(query,conn)





        list_of_Gantt_Data=[]
        i=0
        print("8")
        for order_number,list_date in  zip(df['ORDER#'],df['LIST DATE']):
            # df.loc[df['B'] == 3, 'A'].iloc[0]
            exists = order_number in df_framescutting['J'].values
            if exists:
                count_of_order=df_framescutting.loc[df_framescutting['J'] == order_number,'Count_Column'].iloc[0]

                unique_ids=df_framescutting.loc[df_framescutting['J'] == order_number,'F']

                sum_weld_clean=0
                sum_shipped=0
                sum_pnt_shop_received=0
                sum_vp_received=0
                frameclearing_date_list=[]
                ColourShipping_date_list=[]
                # DVCoartingColourReceiving_date_list=[]
                ExpressCoatingColourReceiving_date_list=[]
                vp_received_date_list=[]
                for id in unique_ids.values:
                    # ------ table FrameClearing --
                    if id in df_frameclearing['Id'].values:
                        frameclearing_date=df_frameclearing.loc[df_frameclearing['Id'] == id,'Date'].iloc[0]
                        frameclearing_date_list.append(frameclearing_date)
                        sum_weld_clean+=1

                    if id in df_ColourShipping['Id'].values:
                        ColourShipping_date=df_ColourShipping.loc[df_ColourShipping['Id'] == id,'Date'].iloc[0]
                        ColourShipping_date_list.append(ColourShipping_date)
                        sum_shipped+=1

                    if id in df_ExpressCoatingColourReceiving['Line'].values:
                        ExpressCoatingColourReceiving_date=df_ExpressCoatingColourReceiving.loc[df_ExpressCoatingColourReceiving['Line'] == id,'Date'].iloc[0]
                        ExpressCoatingColourReceiving_date_list.append(ExpressCoatingColourReceiving_date)
                        sum_pnt_shop_received+=1


                    if id in df_vp_received['Id'].values:
                        vp_received_date=df_vp_received.loc[df_vp_received['Id'] == id,'Date'].iloc[0]
                        vp_received_date_list.append(vp_received_date)
                        sum_vp_received+=1


                # ___CuttingDate___
                start_cutting_date=df_framescutting.loc[df_framescutting['J'] == order_number,'U'].iloc[0]
                start_cutting_date=start_cutting_date.date()
                cutting_date,cutting_color=on_time(start_cutting_date,list_date,setting_object.cutting)
                # Weld/clean


                if len(frameclearing_date_list) !=0:
                    weld_clean_date=sorted(frameclearing_date_list)
                    weld_clean_date=weld_clean_date[0]
                    weld_clean_date,weld_clean_color=on_time(weld_clean_date,list_date,setting_object.weld_clean)
                else:
                    weld_clean_date=0
                    weld_clean_date,weld_clean_color=on_time(weld_clean_date,list_date,setting_object.weld_clean)


                if len(ColourShipping_date_list) !=0:
                    ColourShipping_date=sorted(ColourShipping_date_list)[0]
                    ColourShipping_date,ColourShipping_color=on_time(ColourShipping_date,list_date,setting_object.shipping)
                else:
                    ColourShipping_date=0
                    ColourShipping_date,ColourShipping_color=on_time(ColourShipping_date,list_date,setting_object.shipping)

                if len(ExpressCoatingColourReceiving_date_list) !=0:
                    pnt_receiving_date=sorted(ExpressCoatingColourReceiving_date_list)[0]
                    pnt_receiving_date,pnt_receiving_color=on_time(pnt_receiving_date,list_date,setting_object.pnt_receiving)

                else :
                    pnt_receiving_date=0
                    pnt_receiving_date,pnt_receiving_color=on_time(pnt_receiving_date,list_date,setting_object.pnt_receiving)



                if len(vp_received_date_list) !=0:
                    VP_receiving_date=sorted(vp_received_date_list)[0]
                    VP_receiving_date,VP_receiving_color=on_time(VP_receiving_date,list_date,setting_object.VP_receiving)
                else :
                    VP_receiving_date=0
                    VP_receiving_date,VP_receiving_color=on_time(VP_receiving_date,list_date,setting_object.VP_receiving)


                i+=1
                VP_receiving_ratio =sum_vp_received / count_of_order
                list_of_Gantt_Data.append([order_number,start_cutting_date,sum_weld_clean, sum_shipped, sum_pnt_shop_received, sum_vp_received,list_date.date(),count_of_order,VP_receiving_ratio,cutting_date.date(),cutting_color,weld_clean_date.date(),weld_clean_color,ColourShipping_date.date(),ColourShipping_color,pnt_receiving_date.date(),pnt_receiving_color,VP_receiving_date.date(),VP_receiving_color])

    finally:
        conn.close()

    setting_object= settings_model.objects.all()
    if setting_object :
        setting_object=setting_object[0]

    return render(request,"color_tracking/express_coating.html",{"setting_object":setting_object,"list_of_Gantt_Data":list_of_Gantt_Data})


@login_required
def color_tracking(request):
    print("1")
    conn = MySQLdb.connect(host = "213.190.6.85", user = "u370015874_test", passwd = "Test1234", db = "u370015874_test")
    try:
        print("2")
        cursor = conn.cursor()
        cursor.execute("select * from ordersummary")
        rows = cursor.fetchall()
        sum_of_white_pie,sum_of_color_pie=SumForPieChart(rows,7,47)
        total_sum_pie_chart=sum_of_white_pie+sum_of_color_pie
        sum_of_white_pie_perc=(sum_of_white_pie/total_sum_pie_chart)*100
        sum_of_color_pie_perc=(sum_of_color_pie/total_sum_pie_chart)*100

        sum_of_white_bar,sum_of_color_bar,sum_color_inout_bar=SumForBarChart(rows,7,47)
        total_sum_bar_chart=sum_of_white_bar+sum_of_color_bar+sum_color_inout_bar
        sum_of_white_bar_perc=int((sum_of_white_bar/total_sum_bar_chart)*100)
        sum_of_color_bar_perc=int((sum_of_color_bar/total_sum_bar_chart)*100)
        sum_color_inout_bar_perc=int((sum_color_inout_bar/total_sum_bar_chart)*100)
        piechart_data = [sum_of_white_pie,sum_of_color_pie,sum_of_white_pie_perc,sum_of_color_pie_perc]
        barchart_data = [sum_of_white_bar,sum_of_color_bar,sum_color_inout_bar,sum_of_white_bar_perc,sum_of_color_bar_perc,sum_color_inout_bar_perc]
        cursor=conn.cursor()
        cursor.execute("select COLUMN_NAME as 'name' from information_schema.columns where table_name='ordersummary'")
        print("3")
        all_coloumns_names=cursor.fetchall()
        coloumns_list, progress_list_of_sum_whites, progress_list_of_sum_colors = ProgressChart(rows,all_coloumns_names)
        progress_percentage_list=progress_percentage(progress_list_of_sum_colors,progress_list_of_sum_whites)
        Progress_list_of_all= list_of_all_lists(coloumns_list,progress_list_of_sum_whites,progress_list_of_sum_colors,progress_percentage_list)
        print("4")

        # -----Settings------

        setting_object= settings_model.objects.all()
        if setting_object :
            setting_object=setting_object[0]



        # ________Dataframe part__________
        query = "select * from ordersummary;"
        df = pd.read_sql(query,conn,columns=['ORDER#','LIST DATE'])
        df=df[df['LIST DATE']!='']
        df=df[(df['COLOUR IN']!='WHT') | (df['COLOUR OUT']!='WHT')]

        df = df.sort_values(by="LIST DATE")
        df['LIST DATE'] = pd.to_datetime(df['LIST DATE'])
        Current_Date =pd.to_datetime(datetime.date.today())

        Nextweek_Date =pd.to_datetime(datetime.date.today() + datetime.timedelta(days=setting_object.loading_days))
        mask = (df['LIST DATE'] >= Current_Date) & (df['LIST DATE'] <= Nextweek_Date)
        df = df.loc[mask]
        print("5")
        # ------ table framecutting ----
        query = "select F,J,U,H,L from framescutting;"
        df_framescutting = pd.read_sql(query,conn)
        df_framescutting['U'] = pd.to_datetime(df_framescutting['U'])

        print("6")

        # ----- table FrameClearing ---
        query = "select Id,Date from FrameClearing;"
        print("7")
        df_frameclearing = pd.read_sql(query,conn)

        query = "select Id,Date from ColourShipping;"
        df_ColourShipping = pd.read_sql(query,conn)

        query = "select Id,Date,Line from ExpressCoatingColorReceiving;"
        df_ExpressCoatingColourReceiving = pd.read_sql(query,conn)

        # query = "select Id,Date from DVCoatexColorReceiving;"
        # df_DVCoartingColourReceiving = pd.read_sql(query,conn)

        query = "select Id,Date from ColourReceiving;"
        df_vp_received = pd.read_sql(query,conn)


        exceptions_model =Exceptions.objects.all()
        if exceptions_model:
            for exception in exceptions_model :
                if exception.urban_part != None and exception.window_type != None:
                    df_framescutting = df_framescutting[~(df_framescutting['H'] == exception.urban_part) | (df_framescutting['L'] == exception.window_type)]

                elif exception.window_type == None :
                    df_framescutting = df_framescutting[(df_framescutting['H'] != exception.urban_part)]

                elif exception.urban_part == None :
                    print("urban_part empty")
                    df_framescutting = df_framescutting[(df_framescutting['L'] != exception.window_type)]

        df_framescutting['Count_Column'] = df_framescutting['J'].map(df_framescutting['J'].value_counts())

        list_of_Gantt_Data=[]
        i=0
        print("8")
        for order_number,list_date in  zip(df['ORDER#'],df['LIST DATE']):
            # df.loc[df['B'] == 3, 'A'].iloc[0]
            exists = order_number in df_framescutting['J'].values
            if exists:
                count_of_order=df_framescutting.loc[df_framescutting['J'] == order_number,'Count_Column'].iloc[0]

                unique_ids=df_framescutting.loc[df_framescutting['J'] == order_number,'F']

                sum_weld_clean=0
                sum_shipped=0
                sum_pnt_shop_received=0
                sum_vp_received=0
                frameclearing_date_list=[]
                ColourShipping_date_list=[]
                DVCoartingColourReceiving_date_list=[]
                ExpressCoatingColourReceiving_date_list=[]
                vp_received_date_list=[]
                for id in unique_ids.values:
                    # ------ table FrameClearing --
                    if id in df_frameclearing['Id'].values:
                        frameclearing_date=df_frameclearing.loc[df_frameclearing['Id'] == id,'Date'].iloc[0]
                        frameclearing_date_list.append(frameclearing_date)
                        sum_weld_clean+=1

                    if id in df_ColourShipping['Id'].values:
                        ColourShipping_date=df_ColourShipping.loc[df_ColourShipping['Id'] == id,'Date'].iloc[0]
                        ColourShipping_date_list.append(ColourShipping_date)
                        sum_shipped+=1

                    if id in df_ExpressCoatingColourReceiving['Line'].values:
                        ExpressCoatingColourReceiving_date=df_ExpressCoatingColourReceiving.loc[df_ExpressCoatingColourReceiving['Line'] == id,'Date'].iloc[0]
                        ExpressCoatingColourReceiving_date_list.append(ExpressCoatingColourReceiving_date)
                        sum_pnt_shop_received+=1

                    if id in df_vp_received['Id'].values:
                        vp_received_date=df_vp_received.loc[df_vp_received['Id'] == id,'Date'].iloc[0]
                        vp_received_date_list.append(vp_received_date)
                        sum_vp_received+=1


                # ___CuttingDate___
                start_cutting_date=df_framescutting.loc[df_framescutting['J'] == order_number,'U'].iloc[0]
                start_cutting_date=start_cutting_date.date()
                cutting_date,cutting_color=on_time(start_cutting_date,list_date,setting_object.cutting)
                # Weld/clean


                if len(frameclearing_date_list) !=0:
                    weld_clean_date=sorted(frameclearing_date_list)
                    weld_clean_date=weld_clean_date[0]
                    weld_clean_date,weld_clean_color=on_time(weld_clean_date,list_date,setting_object.weld_clean)
                else:
                    weld_clean_date=0
                    weld_clean_date,weld_clean_color=on_time(weld_clean_date,list_date,setting_object.weld_clean)


                if len(ColourShipping_date_list) !=0:
                    ColourShipping_date=sorted(ColourShipping_date_list)[0]
                    ColourShipping_date,ColourShipping_color=on_time(ColourShipping_date,list_date,setting_object.shipping)
                else:
                    ColourShipping_date=0
                    ColourShipping_date,ColourShipping_color=on_time(ColourShipping_date,list_date,setting_object.shipping)

                if len(ExpressCoatingColourReceiving_date_list) !=0:
                    pnt_receiving_date=sorted(ExpressCoatingColourReceiving_date_list)[0]
                    pnt_receiving_date,pnt_receiving_color=on_time(pnt_receiving_date,list_date,setting_object.pnt_receiving)

                else :
                    pnt_receiving_date=0
                    pnt_receiving_date,pnt_receiving_color=on_time(pnt_receiving_date,list_date,setting_object.pnt_receiving)



                if len(vp_received_date_list) !=0:
                    VP_receiving_date=sorted(vp_received_date_list)[0]
                    VP_receiving_date,VP_receiving_color=on_time(VP_receiving_date,list_date,setting_object.VP_receiving)
                else :
                    VP_receiving_date=0
                    VP_receiving_date,VP_receiving_color=on_time(VP_receiving_date,list_date,setting_object.VP_receiving)


                i+=1
                VP_receiving_ratio =sum_vp_received / count_of_order
                list_of_Gantt_Data.append([order_number,start_cutting_date,sum_weld_clean, sum_shipped, sum_pnt_shop_received, sum_vp_received,list_date.date(),count_of_order,VP_receiving_ratio,cutting_date.date(),cutting_color,weld_clean_date.date(),weld_clean_color,ColourShipping_date.date(),ColourShipping_color,pnt_receiving_date.date(),pnt_receiving_color,VP_receiving_date.date(),VP_receiving_color])

    finally:
        conn.close()

    setting_object= settings_model.objects.all()
    if setting_object :
        setting_object=setting_object[0]

    return render(request,"color_tracking/colortracking.html",{"rows" : rows ,"setting_object":setting_object,"piechart_data": piechart_data, "barchart_data": barchart_data,"Progress_list_of_all":Progress_list_of_all,"list_of_Gantt_Data":list_of_Gantt_Data})

@login_required
def vw_home(request):
    date1=datetime.datetime(2021,1,9)
    date2 = datetime.datetime(2021,4,9)
    t=on_time(date1,date2,10)
    setting_object= settings_model.objects.all()
    if setting_object :
        setting_object=setting_object[0]

    return render(request,"base/home.html",{"setting_object":setting_object})



def vw_login(request):
    message=""
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    if request.POST:
        if request.POST.get("username"):
            username=request.POST.get("username")
            password=request.POST.get("password")
            user = authenticate( username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
               message=""
        else:
            message=""
    return render(request,"base/login.html",{"message":message})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')



def vw_list_users(request):
    all_user=Account.objects.all()
    return render(request,"managment/users.html",{"all_user":all_user})
