"""onlineregappdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.urls import path,include
from adminapp import views

urlpatterns = [
    path('', views.adminloginpage, name="adminloginpage"),
    path('adminvalidation/', views.adminvalidation, name="adminvalidation"),
    path('schedule_new_class/', views.schedule_new_class, name="schedule_new_class"),
    path('View_all_Scheduled_classes/', views.View_all_Scheduled_classes, name="View_all_Scheduled_classes"),
    path('admin_cousre_reg/', views.admin_cousre_reg, name="admin_cousre_reg"),
    path('update_viewall_admin/', views.update_viewall_admin, name="update_viewall_admin"),
    path('delete_viewall_admin/', views.delete_viewall_admin, name="delete_viewall_admin"),
    path('updated_schedule/', views.updated_schedule, name="updated_schedule"),
    path('admin_logout/',views.admin_logout,name="admin_logout")

]

