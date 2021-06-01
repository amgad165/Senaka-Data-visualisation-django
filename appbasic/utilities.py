import MySQLdb
import pandas as pd
import datetime

def SumForPieChart(rows,range1,range2):
    sum_white=0
    sum_color=0
    for row in rows:
        if row[58] == "WHT" and row[59] == "WHT":
            for i in range(range1,range2):
                if row[i]=="" or i == 23 or i == 24 or i ==25:
                    sum_white+=0
                else:
                    sum_white += int(row[i])
        else:
            for i in range(range1,range2):
                if row[i]=="":
                    sum_color+=0
                else:
                    sum_color += int(row[i])
    return sum_white,sum_color

def SumForBarChart(rows,range1,range2):
    sum_white=0
    sum_color=0
    sum_color_inout=0
    for row in rows:
        if row[58] == "WHT" and row[59] == "WHT":
            for i in range(range1,range2):
                if row[i]=="" or i == 23 or i == 24 or i ==25:
                    sum_white+=0
                else:
                    sum_white += int(row[i])
        elif row[58] == "WHT" or row[59] == "WHT":
            for i in range(range1,range2):
                if row[i]=="" or i == 23 or i == 24 or i ==25:
                    sum_color+=0
                else:
                    sum_color += int(row[i])
        else:
            for i in range(range1,range2):
                if row[i]=="" or i == 23 or i == 24 or i ==25:
                    sum_color_inout+=0
                else:
                    sum_color_inout += int(row[i])
    return sum_white,sum_color,sum_color_inout

def ProgressChart(rows,all_coloumns):
    coloumns_list=['AW-V','CS-L','CS-R','V-F','V-SF','SHAPE','DES','V-A','V-B','V-SH','V-SS','SHP-SH','DUMMY','DESLO','SHO','SLO','V-AO','V-BLO','V-SHO','V-SLO','V-SLOS','V-SSO','DWIND','SDWIND','CSHAPE','CAW-V','CCS-L','CECS-L','CECS-R','CV-F','V-C','V-LCS']
    dict_of_coloumn_indexes = dict_of_coloumn_name_indexes(coloumns_list,all_coloumns)
    list_of_sum_whites=[]
    list_of_sum_colors=[]
    index=0
    for coloumn in coloumns_list:
        list_of_sum_whites.append(0)
        list_of_sum_colors.append(0)
        for row in rows:
            if row[58] == "WHT" and row[59] == "WHT":
                if row[dict_of_coloumn_indexes[coloumn]]=="":
                    list_of_sum_whites[index]+=0

                else:
                    list_of_sum_whites[index] += int(row[dict_of_coloumn_indexes[coloumn]])
            else:
                if row[dict_of_coloumn_indexes[coloumn]]=="":
                    list_of_sum_colors[index]+=0

                else:
                    list_of_sum_colors[index] += int(row[dict_of_coloumn_indexes[coloumn]])
        index+=1
    return coloumns_list, list_of_sum_whites, list_of_sum_colors


def dict_of_coloumn_name_indexes(coloumns_list,allColoumns):
    all_coloumns=clean_coloumns(allColoumns)
    dict_of_coloumn_indexes={}
    for coloumn_list in coloumns_list:
        index=0
        for coloumn in all_coloumns:
            if coloumn_list == coloumn:
                dict_of_coloumn_indexes[coloumn_list]=index
            index+=1
    return dict_of_coloumn_indexes

def clean_coloumns(all_coloumns):
    list_of_coloumns =[]
    for coloumn in all_coloumns:
        cleaned_coloumn = coloumn[0]
        list_of_coloumns.append(cleaned_coloumn)
    return list_of_coloumns
def progress_percentage(list1,list2):

    tot = [i + j for i, j in zip(list1, list2)]
    my_new_list = [i / j if j else 0 for i, j in zip(list1, tot)]
    my_new_list = [i * 100 for i in my_new_list]
    return my_new_list
def list_of_all_lists(list1,list2,list3,list4):
    final=[]
    for i in range(len(list1)):
        final.append([list1[i],list2[i],list3[i],list4[i]])
    return final

def get_coloumn_index(coloumn_name,allColoumns):
    all_coloumns=clean_coloumns(allColoumns)
    index=0
    for coloumn_name in all_coloumns:
        if coloumn_name == coloumn:
            dict_of_coloumn_indexes[coloumn_list]=index
        index+=1
    return index

def on_time(actual_date, list_date,settings_rule):

    date =date_by_sub_business_days(list_date,settings_rule)
    if actual_date ==0:
        return date,"red"
    elif actual_date <= date:
        return date,"green"
    elif actual_date > date:
        return date,"yellow"


def date_by_sub_business_days(from_date, sub_days):
    business_days_to_sub= sub_days
    current_date = from_date
    while business_days_to_sub > 0:
        current_date -= datetime.timedelta(days=1)
        weekday = current_date.weekday()
        if weekday >= 5: # sunday = 6
            continue
        business_days_to_sub -= 1
    return current_date

def working_days(days):
    business_days_to_add= days
    current_date = datetime.date.today()
    count=0
    while business_days_to_add > 0:
        count = count+1
        current_date += datetime.timedelta(days=1)
        weekday = current_date.weekday()
        if weekday >= 5: # sunday = 6
            continue
        business_days_to_add -= 1
    return count


(MON, TUE, WED, THU, FRI, SAT, SUN) = range(7)

def workdaysub(start_date,work_days, whichdays=(MON,TUE,WED,THU,FRI)):
    '''
    Adds to a given date a number of working days
    2009/12/04 for example is a friday - adding one weekday
    will return 2209/12/07
    >>> workdayadd(date(year=2009,month=12,day=4),1)
    datetime.date(2009, 12, 7)
    '''
    weeks, days = divmod(work_days,len(whichdays))
    new_date = start_date + datetime.timedelta(weeks=weeks)
    for i in range(days):
        while new_date.weekday() not in whichdays:
            new_date -= datetime.timedelta(days=1)
    return new_date
