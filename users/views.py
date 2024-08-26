from django.shortcuts import render,redirect
from django.http import HttpResponse
from users.forms import EmployeeForms
from django.contrib import messages

def index(request):
    return render(request, 'shared/base.html')

def employeeRegister(request):
    employee_register_form = EmployeeForms()
    if request.method == 'POST':
        employee_register_form = EmployeeForms(request.POST)
        if employee_register_form.is_valid():
            messages.success(request,'Usuario cadastrado com sucesso')
            employee_register_form.save()
            return redirect('index')
    return render(request,'employee_register.html',{'employee_register_form':employee_register_form})     