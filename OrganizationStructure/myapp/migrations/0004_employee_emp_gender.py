# Generated by Django 5.1.6 on 2025-02-28 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_employee_description_employee_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='emp_gender',
            field=models.CharField(blank=True, choices=[('1', 'Male'), ('2', 'Female'), ('3', 'Other')], max_length=20, null=True),
        ),
    ]
