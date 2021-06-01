"""senaka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
from appbasic import views as appbasicviews
from appcustomer import views as appcustomerviews
from appproducts import views as appproductsviews
from django.contrib.staticfiles.urls import static
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', appbasicviews.vw_home),
    path('color_tracking/', appbasicviews.color_tracking, name="color_tracking"),
    path('new_orders/', appbasicviews.new_orders, name="new_orders"),
    path('company_color/', appbasicviews.company_color, name="company_color"),

    path('express_coating/', appbasicviews.express_coating, name="express_coating"),
    path('settings/',appbasicviews.Settings.as_view(template_name="color_tracking/settings.html"), name="settings"),
    path('select_exceptions/',appbasicviews.ExceptionLIST.as_view(template_name="color_tracking/select_exceptions.html"), name="select_exceptions"),
    path('create_exception/',appbasicviews.CreateException.as_view(template_name="color_tracking/create_exception.html"), name="create_exception"),
    path('<pk>/update_exception/',appbasicviews.UpdateException.as_view(template_name="color_tracking/update_exception.html"), name="update_exception"),
    path('<pk>/delete/',appbasicviews.DeleteException.as_view(template_name="color_tracking/exceptions_confirm_delete.html"), name="delete_exception"),

    path('<pk>/update/',appbasicviews.UpdateSettings.as_view(template_name="color_tracking/update_settings.html"), name="update_settings"),
    path('login/', appbasicviews.vw_login, name="login"),
    path("logout/", appbasicviews.logout_view, name="logout"),
    url(r'^accounts/login/$',appbasicviews.vw_login),
    url(r'^accounts/logout/$',appbasicviews.logout_view),
    url(r'^list_customer/$',appcustomerviews.vw_list_customer),
    url(r'^list_doors/$',appproductsviews.vw_list_door),
    url(r'^list_doors_option/$',appproductsviews.vw_list_door_option),
    url(r'^list_window_option/$',appproductsviews.vw_list_window_option),
    url(r'^list_window_type/$',appproductsviews.vw_list_window_type),
    url(r'^list_spacer_type/$',appproductsviews.vw_list_spacer_type),
    url(r'^list_rosettes/$',appproductsviews.vw_list_rosettes),
    url(r'^list_grill_type/$',appproductsviews.vw_list_grill_type),
    url(r'^list_glass_type/$',appproductsviews.vw_list_glass_type),
    url(r'^list_deduction/$',appproductsviews.vw_list_deduction),
    url(r'^list_miscellaneous_1/$',appproductsviews.vw_list_miscellaneous_1),
    url(r'^list_miscellaneous_2/$',appproductsviews.vw_list_miscellaneous_2),
    url(r'^list_miscellaneous_3/$',appproductsviews.vw_list_miscellaneous_3),
    url(r'^list_miscellaneous_4/$',appproductsviews.vw_list_miscellaneous_4),
    url(r'^list_miscellaneous_5/$',appproductsviews.vw_list_miscellaneous_5),
    url(r'^list_miscellaneous_6/$',appproductsviews.vw_list_miscellaneous_6),
    url(r'^list_window_minmax/$',appproductsviews.vw_list_window_minmax),
    url(r'^list_color_price/$',appproductsviews.vw_list_color_price),
    url(r'^list_part_price/$',appproductsviews.vw_list_part_price),
    url(r'^list_window_item/$',appproductsviews.vw_list_window_item),
    url(r'^list_users/$',appbasicviews.vw_list_users),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
