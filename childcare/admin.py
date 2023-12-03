from django.contrib import admin

class FacilityAdminSite(admin.AdminSite):
    site_header = 'Facility Admin'
    site_title = 'Facility Admin '




FacilityAdminSite = FacilityAdminSite(name='FacilityAdminSite')


