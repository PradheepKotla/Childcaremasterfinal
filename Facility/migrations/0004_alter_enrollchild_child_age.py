# Generated by Django 4.2.5 on 2023-11-18 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facility', '0003_remove_assigntoclassroom_classes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollchild',
            name='child_age',
            field=models.CharField(blank=True, choices=[('infant', 'infant'), ('toddler', 'toddler'), ('twaddler', 'twaddler'), ('three_years_old', 'three_years_old'), ('four_years_old', 'four_years_old')], max_length=100),
        ),
    ]
