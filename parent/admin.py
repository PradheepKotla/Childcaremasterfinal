from django.contrib import admin
from .models import Payment
from childcare.admin import FacilityAdminSite
# Register your models here.

admin.site.register(Payment)


FacilityAdminSite.register(Payment)
