from django import template
from django.contrib.auth.models import Group
from appbasic.models import Account

def groups(request):
    user_groups = list(request.user.groups.values_list('name',flat = True)) 
    return {'user_groups': user_groups}
