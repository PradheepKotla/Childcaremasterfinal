# Generated by Django 4.2.5 on 2023-11-19 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Facility', '0007_hirestaff_hours_worked'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hirestaff',
            old_name='houly_salary',
            new_name='hourly_salary',
        ),
    ]
