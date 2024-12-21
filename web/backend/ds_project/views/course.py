from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from django.core import serializers
from ..models.course import Course
import copy
import json

class GetCourseAPIView(GenericAPIView):
    def get(self, request):
        params = request.query_params
        try:
            course_id = params['course_id']
        except:
            return Response(
                {
                    "success": False,
                    "message": "Thông tin môn học không hợp lệ"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if not course_id or len(course_id) == 0:
            return Response(
                {
                    "success": False,
                    "message": "Mã môn học không hợp lệ"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            course_instance = Course.objects.get(course_id=course_id)
        except Course.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Môn học không tồn tại"
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
        
        copy_instance = copy.deepcopy(course_instance)
        json_data = json.loads(serializers.serialize('json', [copy_instance]))

        return Response(
            {
                "success": True,
                "message": "Truy xuất môn học thành công",
                "data": json_data[0].get('fields', None)
            }, 
            status=status.HTTP_200_OK
        )