from rest_framework.serializers import ModelSerializer
from Facility.models import EnrollChild
from .models import Payment



class ChildrenSerializer(ModelSerializer):
    class Meta:
        model = EnrollChild
        fields = "__all__"


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
