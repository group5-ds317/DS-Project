from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from ..models.major import Major
from django.core import serializers
import copy
import json
    
class GetMajorAPIView(GenericAPIView):
    def get(self, request):
        params = request.query_params
        try:
            major_id = params['major_id']
        except:
            return Response(
                {
                    "success": False,
                    "message": "Thông tin ngành học không hợp lệ"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
     
        if not major_id or len(major_id) == 0:
            return Response(
                {
                    "success": False,
                    "message": "Mã ngành học không hợp lệ"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
     
        try:
            instance = Major.objects.get(major_id=major_id)
        except Major.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Ngành học không tồn tại"
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
                "message": "Truy xuất thành công",
                "data": json_data[0].get('fields', None)
            }, 
            status=status.HTTP_200_OK
        )