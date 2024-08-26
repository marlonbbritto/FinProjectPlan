from django import forms

from users.models import Employee

class EmployeeForms(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'name':'Nome completo do colaborador',
            'company_email':'Email corporativo',
            'personal_email':'Email pessoal',
            'position':'Cargo do colaborador',
            'salary':'Salario CLT do colaborador',
            'additional_benefits_values':'Valores de beneficios adicionais',
            'health_plan_values':'Valores de beneficios de plano de saúde',
        }
        widgets = {
            'name':forms.TextInput(
                attrs={
                    'type':"text",
                    'class':"form-control",
                    'id':"floatingInput",
                    'placeholder':'João Silva',
                }
            ),
            'company_email':forms.EmailInput(
                attrs={
                    'type':"email",
                    'class':'form-control',
                    'id':"floatingInput",
                    'placeholder':"name@example.com"
                }
            ),
            'personal_email':forms.EmailInput(
                attrs={
                    'type':"email",
                    'class':'form-control',
                    'id':"floatingInput",
                    'placeholder':"name@example.com"
                }
            ),
            'position':forms.TextInput(
                attrs={
                    'type':"text",
                    'class':"form-control",
                    'id':"floatingInput",
                    'placeholder':'João Silva',
                }
            ),
            'salary':forms.NumberInput(
                attrs={
                    'type':"number",
                    'class':"form-control",
                    'id':"floatingInput",
                    'placeholder':'10000,00',
                }
            ),
            'additional_benefits_values':forms.NumberInput(
                attrs={
                    'type':"number",
                    'class':"form-control",
                    'id':"floatingInput",
                    'placeholder':'10000,00',
                }
            ),
            'health_plan_values':forms.NumberInput(
                attrs={
                    'type':"number",
                    'class':"form-control",
                    'id':"floatingInput",
                    'placeholder':'10000,00',
                }
            ),
        }