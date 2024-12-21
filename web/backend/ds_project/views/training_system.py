from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from ..models.training_system import TrainingSystem
from django.core import serializers
import copy
import json
    
class GetTrainingSystemAPIView(GenericAPIView):
    def get(self, request):
        params = request.query_params
        try:
            training_system_id = params['training_system_id']
        except:
            return Response(
                {
                    "success": False,
                    "message": "Thông tin hệ đào tạo không hợp lệ"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
     
        if not training_system_id or len(training_system_id) == 0:
            return Response(
                {
                    "success": False,
                    "message": "Mã hệ đào tạo không hợp lệ"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
     
        try:
            instance = TrainingSystem.objects.get(training_system_id=training_system_id)
        except TrainingSystem.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Hệ đào tạo không tồn tại"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except:
            return Response(
                {
                    "success": False,
                    "message": "Lỗi Database"
                }, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        copy_instance = copy.deepcopy(instance)
        json_data = json.loads(serializers.serialize('json', [copy_instance]))
    
        return Response(
            {
                "success": True,
                "message": "Truy xuất hệ đào tạo thành công",
                "data": json_data[0].get('fields', None)
            }, 
            status=status.HTTP_200_OK
        )