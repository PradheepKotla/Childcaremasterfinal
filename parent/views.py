from django.shortcuts import render
from Facility.models import EnrollChild
from .serializer import ChildrenSerializer,PaymentSerializer
from rest_framework.views import APIView
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Payment
# Create your views here.

class ChildrenApiview(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
            
        try:
            return EnrollChild.objects.get(pk=pk)
        except EnrollChild.DoesNotExist:
            raise Http404
       
    def get(self, request, pk=None, format=None):
        current_user = request.user
        if pk:
            data = self.get_object(pk)
            serializer = ChildrenSerializer(data)
            return Response(serializer.data)

        else:
            data = EnrollChild.objects.filter(user=current_user)
            serializer = ChildrenSerializer(data, many=True)
            if not data.exists():
                return Response({'detail': 'No children found for the current user'}, status=status.HTTP_404_NOT_FOUND)

            return Response(serializer.data)
       
    def post(self, request, format=None):
        data = request.data.copy()

        user = request.user  
       
        data['user'] = user.id  # Assuming your serializer expects a user ID

        child_age = data.get('child_age', None)
        if child_age:
            max_allowed_children = {
                'infant' : 8,
                'toddler': 12,
                'twaddler': 16,
                'three_years_old': 18,
                'four_years_old': 20,
            }
            if child_age in max_allowed_children:
                # Check if the maximum allowed children of this age group is reached
                current_children_count = EnrollChild.objects.filter(child_age=child_age).count()
                if current_children_count >= max_allowed_children[child_age]:
                    # If the limit is reached, set waiting_list to True
                    data['waiting_list'] = True

        serializer = ChildrenSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        

        serializer.save(user=user)

        response = Response()

        response.data = {
            'message': 'child Created Successfully',
            'data': serializer.data
        }

        return response
       
    def patch(self, request, pk=None, format=None):
                
        todo_to_update = EnrollChild.objects.get(pk=pk)

        serializer = ChildrenSerializer(instance=todo_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()

        response.data = {
            'message': 'child data is Successfully updated',
            'data': serializer.data
        }

        return response
      
        
        


class PaymentAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        data = request.data.copy()

        user = request.user  
       
        data['user'] = user.id  
        serializer = PaymentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        

        serializer.save(user=user)

        response = Response()

        response.data = {
            'message': 'payment Created Successfully',
            'data': serializer.data
        }

        return response


        
    
    def get(self, request, pk=None, format=None):
            current_user = request.user
            if pk:
                data = self.get_object(pk)
                serializer = PaymentSerializer(data)
                return Response(serializer.data)

            else:
                data = Payment.objects.filter(user=current_user)
                serializer = PaymentSerializer(data, many=True)
                if not data.exists():
                    return Response({'detail': 'No Payments found for the current user'}, status=status.HTTP_404_NOT_FOUND)

                return Response(serializer.data)