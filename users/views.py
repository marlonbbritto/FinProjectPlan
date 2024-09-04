from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from users.forms import EmployeeForms,UserCreationForm
from users.models import Employee,UserData

def index(request):
    return render(request, 'shared/base.html')

def employee_register(request):
    if request.method == 'POST':
        employee_register_form = EmployeeForms(request.POST)
        if employee_register_form.is_valid():
            company_email = employee_register_form.cleaned_data.get('company_email')
            if Employee.objects.filter(company_email=company_email).exists():
                messages.error(request, 'Esse e-mail já está registrado')
                return redirect('employeeRegister')
            else:
                messages.success(request, 'Usuário cadastrado com sucesso')
                employee_register_form.save()
                return redirect('index')
    else:
        employee_register_form = EmployeeForms()

    return render(request, 'employee_register.html', {'employee_register_form': employee_register_form})

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            employee = form.cleaned_data.get('employee')
            # Criar o UserData associado
            user_data = UserData.objects.create(user=user, employee=employee)
            return redirect('index')  # Redirecionar para alguma página de sucesso
    else:
        form = UserCreationForm()
    return render(request, 'user_register.html', {'form': form})

        
