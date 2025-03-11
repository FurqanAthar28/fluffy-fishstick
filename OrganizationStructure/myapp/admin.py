from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','emp_name','emp_email','emp_education','emp_academic_discipline','age',
                  'emp_contact','emp_gender','date_of_birth','work_status','emp_designation',
                  'emp_department','emp_salary','description']

@admin.register(Manager)    
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['id','manager_name','manager_email','manager_education','manager_academic_discipline',
                    'manager_contact','manager_gender','date_of_birth','work_status','age',
                    'manager_designation','manager_department','manager_salary','description']    