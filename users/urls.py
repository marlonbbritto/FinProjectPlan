from django.contrib import admin
from django.urls import path,include
from users.views import index,employeeRegister

urlpatterns = [
    path('', index, name='index'),
    path('employeeRegister', employeeRegister,name='employeeRegister'),
]