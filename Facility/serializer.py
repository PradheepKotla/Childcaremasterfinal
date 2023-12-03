from rest_framework.serializers import ModelSerializer

from .models import HireStaff



class HireStaffSerializer(ModelSerializer):
    class Meta:
        model = HireStaff
        fields = "__all__"


