# Generated by Django 5.1.6 on 2025-03-08 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_employee_age_manager_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='salary_tax',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
