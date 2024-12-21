from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from ..models.faculty import Faculty
from django.core import serializers
import copy
import json
    
class GetFacultyAPIView(GenericAPIView):
    def get(self, request):
        params = request.query_params
        try:
            faculty_id = params['faculty_id']
        except:
            return Response(
                {
                    "success": False,
                    "message": "Thông tin khoa không hợp lệ"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
     
        if not faculty_id or len(faculty_id) == 0:
            return Response(
                {
                    "success": False,
                    "message": "Mã khoa không hợp lệ"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
     
        try:
            instance = Faculty.objects.get(faculty_id=faculty_id)
        except Faculty.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Khoa không tồn tại"
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