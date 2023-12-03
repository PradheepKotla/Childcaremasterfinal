from django.db import models
from accounts.models import User
from datetime import datetime
# Create your models here.



AGE_CHOICES = [
        ('infant', 'infant'),
        ('toddler', 'toddler'),
        ('twaddler', 'twaddler'),
        ('three_years_old', 'three_years_old'),
        ('four_years_old', 'four_years_old'),
        # Add more choices as needed
    ]
class EnrollChild(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    child_age = models.CharField(max_length=100,blank=True,choices=AGE_CHOICES)
    child_fees = models.IntegerField(null=True)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    parent_name = models.CharField(max_length=100)
    parent_phone_number = models.BigIntegerField()
    allergies = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    consent_form = models.FileField(default=False)
    waiting_list = models.BooleanField(default=False)


class HireStaff(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    frist_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    phone_number = models.BigIntegerField()
    hourly_salary = models.IntegerField()
    earned_salary = models.FloatField(null=True,blank=True)
    terminate = models.BooleanField(default=False)
    hours_worked = models.FloatField(default=0)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.frist_name
    

    def calculate_hours_worked(self):
        if self.start_time is not None and self.end_time is not None:
           
            start_datetime = datetime.combine(datetime.today(), self.start_time)
            end_datetime = datetime.combine(datetime.today(), self.end_time)

           
            time_difference = end_datetime - start_datetime

           
            self.hours_worked = time_difference.total_seconds() / 3600
        else:
           
            self.hours_worked = None

        return self.hours_worked

    def calculate_earned_salary(self):
        if self.hours_worked is not None:
           
            self.earned_salary += self.hours_worked * (self.hourly_salary / 60)  
        else:
           
            self.earned_salary = None

        return self.earned_salary

    def save(self, *args, **kwargs):
        
        self.calculate_hours_worked()

      
        super().save(*args, **kwargs)

        
        self.calculate_earned_salary()
        
        super().save(*args, **kwargs)



class AssignToClassroom(models.Model):
    staff = models.ForeignKey(HireStaff,on_delete=models.CASCADE)
    #classes = models.ForeignKey(ClassRoom,on_delete=models.CASCADE)
    classroom = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.classroom



