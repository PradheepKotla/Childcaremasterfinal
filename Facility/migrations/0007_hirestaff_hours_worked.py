# Generated by Django 4.2.5 on 2023-11-19 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facility', '0006_hirestaff_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='hirestaff',
            name='hours_worked',
            field=models.FloatField(default=0),
        ),
    ]