from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    name = models.CharField(max_length=150,blank=False,null=False)
    company_email = models.EmailField(max_length=150,blank=False,null=False,unique=True)
    personal_email= models.EmailField(max_length=150,blank=True,null=True)
    position=models.CharField(max_length=100,blank=False,null=False)
    salary=models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False)
    additional_benefits_values=models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False)
    health_plan_values=models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
         ordering = ['name']
    def __str__(self):
        return self.name

class UserData(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    employee = models.OneToOneField(Employee,on_delete=models.SET_NULL, null=True)

    def __str__(self):
            return self.user.username

