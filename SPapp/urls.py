from unicodedata import name
from django import views
from django.urls import path
from SPapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('login_view',views.login_view,name='login_view'),
    path('student_reg_form/',views.studentregform,name='student_reg_form'),
    path('studentdetails/',views.studentdetails,name='studentdetails'),
]