from django import forms
from django.contrib.auth.models import User

from users.models import Employee,UserData

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
class UserCreationForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Nome de usuário',
                'type':"text",
                'id':"floatingInput",
                
                
            }
            
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Email',
                'type':"email",
                'id':"floatingInput",                
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Senha',        
                'type':"password",
                'id':"floatingInput",                
                }
            )
    )
    employee = forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Selecione o Empregado',
                'id':"floatingInput", 
                }
            ),
        label='Empregado',
        to_field_name='company_email'  # Mostrar o `company_email` no dropdown
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Configurar a senha corretamente
        if commit:
            user.save()
        return user