import datetime
from .models import *
from datetime import date,datetime
from rest_framework import serializers
from django.core.validators import MinLengthValidator

class EmployeeSerializer(serializers.ModelSerializer):
    date_of_birth = serializers.DateField(write_only=True)
    work_status = serializers.BooleanField(read_only=True)
    emp_email=serializers.EmailField(required=True)
    emp_salary=serializers.DecimalField(required=False,max_digits=10, decimal_places=2)
    salary_tax=serializers.SerializerMethodField('salary_tax_employee')
   
    
    
    class Meta:
        model = Employee
        fields = "__all__" 
        
    
            
    def salary_tax_employee(self, obj):
      if obj.emp_salary is None :
          salary_tax = 0
      else:
       salary=obj.emp_salary
       salary_tax=float(salary)*0.10
      
      return salary_tax
   
    def validate(self, data):
        
        dob = data.get('date_of_birth')
        
        
        if dob is not None:  
            today = date.today()
            calculated_age = today.year - dob.year
            data['age'] = calculated_age
       
        return data


# class EmployeeSerializer2(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = ['emp_name', 'emp_email', 'emp_designation', 'emp_department']


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = "__all__"




