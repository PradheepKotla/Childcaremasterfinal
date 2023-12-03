from django.urls import path,include
from .views import HireStaffAPIview

urlpatterns = [
     path('teacher/', HireStaffAPIview.as_view(),name="HireStaffAPIview"),
     path('teacher/<int:pk>/', HireStaffAPIview.as_view(),name="HireStaffAPIview"),
    

]
