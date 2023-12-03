from django.urls import path,include
from .views import ChildrenApiview,PaymentAPIView

urlpatterns = [
     path('child/', ChildrenApiview.as_view(),name="ChildrenApiview"),
     path('child/<int:pk>/', ChildrenApiview.as_view(),name="ChildrenApiview"),
     path('payment/', PaymentAPIView.as_view(),name="PaymentAPIView"),
     path('payment/<int:pk>/', PaymentAPIView.as_view(),name="PaymentAPIView"),

]
