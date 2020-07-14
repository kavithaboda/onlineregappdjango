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
from student import views

urlpatterns = [
 path('',views.studenthome,name='home'),
        path('student_reg/',views.student_reg,name="student_reg"),
        path('student_login/',views.student_login,name="student_login"),
        path('student_search/',views.student_search,name="student_search"),
        path('student_contactus/',views.student_contactus,name="student_contactus"),
        path('student_registred_process/',views.student_registred_process,name="student_registred_process"),
        path('student_page/',views.student_page,name="student_page"),
        path('enrol_course/',views.enrol_course,name="enrol_course"),
        path('enrolling_process/',views.enrolling_process,name="enrolling_process"),
        path('Viewall_the_enrolled_courses/',views.Viewall_the_enrolled_courses,name="Viewall_the_enrolled_courses"),
       path('cancel_enrolled_courses/',views.cancel_enrolled_courses,name="cancel_enrolled_courses"),
       path('student_logout/',views.student_logout,name="student_logout"),
       path('cancelling_enrolled_course/',views.cancelling_enrolled_course,name="cancelling_enrolled_course")
]
