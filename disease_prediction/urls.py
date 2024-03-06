"""disease_prediction URL Configuration

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
from django.urls import path
from predict import views
# from  predict.views import GeneratePDF
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base, name="base"),
    # path('index/', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('prediction/', views.prediction, name="prediction"),
    path('report/', views.report, name="report"),
    path('myReports/', views.myReports, name="myReports"),
    path('admin_home/', views.admin_home, name="admin_home"),
    path('doctor_home/', views.doctor_home, name="doctor_home"),
    path('search/', views.search, name="search"),
    path('genrate_report/', views.genrate_report, name="genrate_report"),
    path('view_user/', views.view_user, name="view_user"),
    path('views_doctor/', views.view_doctor, name="views_doctor"),
    path('user_home/', views.user_home, name="user_home"),
    path('doctor_patient/', views.doctor_patient, name="doctor_patient"),
    path('hospitalhistory/', views.hospitalhistory, name="hospitalhistory"),


    # Auth
    path('signup/', views.signupuser, name="signupuser"),
    path('login/', views.loginuser, name="loginuser"),
    path('logout/', views.logoutuser, name="logoutuser"),
    path('doctor_logout/', views.doctor_logout, name="doctor_logout"),
     
    path('doctor_login/', views.doctor_login, name="doctor_login"),
    path('doctor_registration/', views.doctor_registration, name="doctor_registration"),
    path('admin_registration/', views.admin_registration, name="admin_registration"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)