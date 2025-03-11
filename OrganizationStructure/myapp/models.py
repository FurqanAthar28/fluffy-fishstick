import datetime
from django.db import models
from django.core.validators import RegexValidator


Choice = (
    ('Male', 'M'),
    ('Female', 'F'),
    ('Other', 'Other')
)

class Employee(models.Model):
    emp_name = models.CharField(max_length=30)
    emp_email = models.EmailField(max_length=30, unique=True, null=True, blank=True,
        error_messages={'unique': "This email has already been registered."}
    )
    emp_education = models.CharField(max_length=100, null=True, blank=True)
    emp_academic_discipline = models.CharField(max_length=100, null=True, blank=True)
    emp_contact = models.CharField(
        max_length=11, null=True, blank=True,
        validators=[    
            RegexValidator(
                regex=r'^0\d{10}$',  
                message='Contact number must start with 0 and be 11 digits long',
                code='invalid_contact'
            )
        ]
    )
    emp_gender = models.CharField(max_length=20, choices=Choice, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    work_status = models.BooleanField(default=True, null=True, blank=True)
    emp_designation = models.CharField(max_length=100)
    emp_department = models.CharField(max_length=100)
    emp_salary = models.FloatField(null=True,blank=True)
    description = models.TextField(blank=True, null=True)
    


class Manager(models.Model):
    manager_name = models.CharField(max_length=30)
    manager_email = models.EmailField(max_length=30, unique=True, null=True, blank=True,
        error_messages={'unique': "This email has already been registered."}
    )
    manager_education = models.CharField(max_length=100, null=True, blank=True)
    manager_academic_discipline = models.CharField(max_length=100, blank=True)
    manager_contact = models.CharField( 
        max_length=11, null=True, blank=True,
        validators=[
            RegexValidator(
                regex=r'^0\d{10}$',
                message='Contact number must start with 0 and be 11 digits long',
                code='invalid_contact'
            )
        ]
    )
    manager_gender = models.CharField(max_length=20, choices=Choice, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)  
    work_status = models.BooleanField(default=True, null=True, blank=True)
    manager_designation = models.CharField(max_length=100)
    manager_department = models.CharField(max_length=100)
    manager_salary = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)

    
