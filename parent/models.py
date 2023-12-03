from django.db import models
from accounts.models import User
from Facility.models import EnrollChild
# Create your models here.

class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    child = models.ForeignKey(EnrollChild,on_delete=models.CASCADE)
    price = models.IntegerField()
    status = models.BooleanField(default=False)
    card_no = models.CharField(max_length=17,blank=True)
    month = models.CharField(max_length=5,blank=True)
    year = models.CharField(max_length=5,blank=True)
    name_on_card = models.CharField(max_length=100,blank=True)

