from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from appproducts.models import *
# Create your views here.
@login_required
def vw_list_door(request):
    list_door=""
    if request.user.is_superuser or request.user.is_staff:
        list_door=mdl_patio_door.objects.all().order_by("patio_door_id")
    return render(request,"managment/doors.html",{"list_door":list_door})

@login_required
def vw_list_door_option(request):
    list_door_option=""
    if request.user.is_superuser or request.user.is_staff:
        list_door_option=mdl_door_option.objects.all().order_by("door_option_id")
    return render(request,"managment/door_options.html",{"list_door_option":list_door_option})


@login_required
def vw_list_window_option(request):
    list_window_option=""
    if request.user.is_superuser or request.user.is_staff:
        list_window_option=mdl_window_option.objects.all().order_by("window_option_id")
    return render(request,"managment/window_options.html",{"list_window_option":list_window_option})


@login_required
def vw_list_spacer_type(request):
    list_spacer_type=""
    if request.user.is_superuser or request.user.is_staff:
        list_spacer_type=mdl_spacer_type.objects.all().order_by("spacer_type_id")
    return render(request,"managment/spacer_type.html",{"list_spacer_type":list_spacer_type})

@login_required
def vw_list_rosettes(request):
    list_rosettes=""
    if request.user.is_superuser or request.user.is_staff:
        list_rosettes=mdl_rosettes.objects.all().order_by("rosettes_id")
    return render(request,"managment/rosettes.html",{"list_rosettes":list_rosettes})

@login_required
def vw_list_grill_type(request):
    list_grill_type=""
    if request.user.is_superuser or request.user.is_staff:
        list_grill_type=mdl_grill_type.objects.all().order_by("grill_type_id")
    return render(request,"managment/grill_type.html",{"list_grill_type":list_grill_type})

@login_required
def vw_list_window_type(request):
    list_window_type=""
    if request.user.is_superuser or request.user.is_staff:
        list_window_type=mdl_window_type.objects.all().order_by("name")
    return render(request,"managment/window_type.html",{"list_window_type":list_window_type})

@login_required
def vw_list_glass_type(request):
    list_glass_type=""
    if request.user.is_superuser or request.user.is_staff:
        list_glass_type=mdl_glass_type.objects.all().order_by("glass_type_id")
    return render(request,"managment/glass_type.html",{"list_glass_type":list_glass_type})


@login_required
def vw_list_deduction(request):
    list_deduction=""
    if request.user.is_superuser or request.user.is_staff:
        list_deduction=mdl_deductions.objects.all().order_by("ln")
    return render(request,"managment/list_deduction.html",{"list_deduction":list_deduction})

@login_required
def vw_list_miscellaneous_1(request):
    list_miscellaneous=""
    if request.user.is_superuser or request.user.is_staff:
        list_miscellaneous=mdl_miscellaneous_1.objects.all().order_by("miscellaneous_id")
    return render(request,"managment/miscellaneous.html",{"list_miscellaneous":list_miscellaneous,"name":"Miscellaneous-1"})

@login_required
def vw_list_miscellaneous_2(request):
    list_miscellaneous=""
    if request.user.is_superuser or request.user.is_staff:
        list_miscellaneous=mdl_miscellaneous_2.objects.all().order_by("miscellaneous_id")
    return render(request,"managment/miscellaneous.html",{"list_miscellaneous":list_miscellaneous,"name":"Miscellaneous-2"})

@login_required
def vw_list_miscellaneous_3(request):
    list_miscellaneous=""
    if request.user.is_superuser or request.user.is_staff:
        list_miscellaneous=mdl_miscellaneous_3.objects.all().order_by("miscellaneous_id")
    return render(request,"managment/miscellaneous.html",{"list_miscellaneous":list_miscellaneous,"name":"Miscellaneous-3"})

@login_required
def vw_list_miscellaneous_4(request):
    list_miscellaneous=""
    if request.user.is_superuser or request.user.is_staff:
        list_miscellaneous=mdl_miscellaneous_4.objects.all().order_by("miscellaneous_id")
    return render(request,"managment/miscellaneous.html",{"list_miscellaneous":list_miscellaneous,"name":"Miscellaneous-4"})

@login_required
def vw_list_miscellaneous_5(request):
    list_miscellaneous=""
    if request.user.is_superuser or request.user.is_staff:
        list_miscellaneous=mdl_miscellaneous_5.objects.all().order_by("miscellaneous_id")
    return render(request,"managment/miscellaneous.html",{"list_miscellaneous":list_miscellaneous,"name":"Miscellaneous-5"})

@login_required
def vw_list_miscellaneous_6(request):
    list_miscellaneous=""
    if request.user.is_superuser or request.user.is_staff:
        list_miscellaneous=mdl_miscellaneous_6.objects.all().order_by("miscellaneous_id")
    return render(request,"managment/miscellaneous.html",{"list_miscellaneous":list_miscellaneous,"name":"Miscellaneous-6"})

@login_required
def vw_list_window_minmax(request):
    list_window_minmax=""
    if request.user.is_superuser or request.user.is_staff:
        list_window_minmax=mdl_window_maxmin.objects.all().order_by("window_type")
    return render(request,"managment/window_minmax.html",{"list_window_minmax":list_window_minmax})

@login_required
def vw_list_color_price(request):
    list_color_price=""
    if request.user.is_superuser or request.user.is_staff:
        list_color_price=mdl_color_price.objects.all().order_by("window_type")
    return render(request,"managment/color_price.html",{"list_color_price":list_color_price})

@login_required
def vw_list_part_price(request):
    list_part_price=""
    if request.user.is_superuser or request.user.is_staff:
        list_part_price=mdl_part_price.objects.all().order_by("multipoint_lock")
    return render(request,"managment/part_price.html",{"list_part_price":list_part_price})

@login_required
def vw_list_window_item(request):
    list_window_item=""
    if request.user.is_superuser or request.user.is_staff:
        list_window_item=mdl_window_item.objects.all().order_by("item_number")
    return render(request,"managment/window_item.html",{"list_window_item":list_window_item})