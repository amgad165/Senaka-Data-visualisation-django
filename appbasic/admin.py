from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from appbasic.models import Account,Settings,OrderEntry,date_range
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('name', 'username', 'email', 'phone', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('name', 'username', 'email', 'phone',)
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('-date_joined', )
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
admin.site.register(Settings)
admin.site.register(OrderEntry)
admin.site.register(date_range)
