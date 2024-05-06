"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from mpr import views

urlpatterns = [
    
    path('',views.index),
    path('register',views.register),
    path('Employee_register',views.Employee_register),
    path('login_1',views.login_1),
    #admin
    path('adminhome',views.adminhome),
    path('admin_view_employee',views.admin_view_employee),
    path('admin_view_users',views.admin_view_users),
    path('actionusers',views.actionusers),
    path('rejectusers',views.rejectusers),

    path('actionemployee',views.actionemployee),
    path('rejectemployee',views.rejectemployee),
    path('deleteemployee',views.deleteemployee),
    path('deleteusers',views.deleteusers),
    path('admin_vieworders',views.admin_vieworders),
    path('admin_add_employee',views.admin_add_employee),
    path('add_emp',views.add_emp),
    
    #user
    
    path('userhome',views.userhome),
    path('addrequest',views.addrequest),
    path('viewrequest_user',views.viewrequest_user),
    path('cancel',views.cancel),
    path('addpayment',views.addpayment),
    path('view_services',views.view_services),

    #employee
    path('employeehome',views.employeehome),
    path('employee_viewrequest',views.employee_viewrequest),
    path('actionrequest',views.actionrequest),
    path('viewpayment',views.viewpayment),
    
    ]
