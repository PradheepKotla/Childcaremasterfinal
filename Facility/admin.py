from django.contrib import admin
from .models import *
from childcare.admin import FacilityAdminSite
# Register your models here.

admin.site.register(AssignToClassroom)
# admin.site.register(ClassRoom)
admin.site.register(EnrollChild)
admin.site.register(HireStaff)

FacilityAdminSite.register(AssignToClassroom)
FacilityAdminSite.register(EnrollChild)
FacilityAdminSite.register(HireStaff)
