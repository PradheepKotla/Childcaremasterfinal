from Facility.models import HireStaff
from .serializer import HireStaffSerializer
from rest_framework.views import APIView
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import HireStaff


class HireStaffAPIview(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
            
        try:
            return HireStaff.objects.get(pk=pk)
        except HireStaff.DoesNotExist:
            raise Http404
       
    def get(self, request, pk=None, format=None):
        current_user = request.user
        if pk:
            data = self.get_object(pk)
            serializer = HireStaffSerializer(data)
            return Response(serializer.data)

        else:
            data = HireStaff.objects.filter(user=current_user).first()
            serializer = HireStaffSerializer(data)

            return Response(serializer.data)
        
    
    def patch(self, request, pk=None, format=None):
                
        todo_to_update = HireStaff.objects.get(pk=pk)

        serializer = HireStaffSerializer(instance=todo_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()

        response.data = {
            'message': 'child data is Successfully updated',
            'data': serializer.data
        }

        return response



   
    


       
