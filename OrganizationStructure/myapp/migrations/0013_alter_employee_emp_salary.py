# Generated by Django 5.1.6 on 2025-03-10 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_remove_employee_salary_tax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_salary',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
