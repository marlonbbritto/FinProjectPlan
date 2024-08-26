from django.contrib import admin

from users.models import Employee

class ListEmployee(admin.ModelAdmin):
    list_display=('id','name','company_email','personal_email','position','salary','additional_benefits_values','health_plan_values')
    list_display_links=('id','name','company_email')
admin.site.register(Employee,ListEmployee)