# Generated by Django 4.2.5 on 2023-11-18 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facility', '0002_enrollchild_user_alter_classroom_four_years_old_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assigntoclassroom',
            name='classes',
        ),
        migrations.AddField(
            model_name='enrollchild',
            name='child_age',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='enrollchild',
            name='child_fees',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='ClassRoom',
        ),
    ]