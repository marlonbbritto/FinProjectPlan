from django.contrib import admin
from django.urls import path,include
from users.views import index,employee_register,user_register

urlpatterns = [
    path('', index, name='index'),
    path('employeeRegister', employee_register,name='employeeRegister'),
    path('user_register',user_register,name='user_register')
]