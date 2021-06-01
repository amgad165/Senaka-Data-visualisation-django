from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from appcustomer.models import mdl_customer
# Create your views here.
@login_required
def vw_list_customer(request):
    list_customer=""
    if request.user.is_superuser:
        list_customer=mdl_customer.objects.all()
    return render(request,"managment/customers.html",{"list_customer":list_customer})
