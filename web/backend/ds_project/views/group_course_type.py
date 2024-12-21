from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from django.core import serializers
from ..models.group_course_type import GroupCourseType
import copy
import json

class GetGroupCourseTypeAPIView(GenericAPIView):
    def get(self, request):
        params = request.query_params
        try:
            group_course_type_id = params['group_course_type_id']
        except:
            return Response(
                {
                    "success": False,
                    "message": "Thông tin nhóm loại môn học không hợp lệ"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if not group_course_type_id or len(group_course_type_id) == 0:
            return Response(
                {
                    "success": False,
                    "message": "Mã nhóm loại môn học không hợp lệ"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            group_course_type_instance = GroupCourseType.objects.get(group_course_type_id=group_course_type_id)
        except GroupCourseType.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Mã nhóm loại môn học không tồn tại"
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
        
        copy_instance = copy.deepcopy(group_course_type_instance)
        json_data = json.loads(serializers.serialize('json', [copy_instance]))

        return Response(
            {
                "success": True,
                "message": "Truy xuất nhóm loại môn học thành công",
                "data": json_data[0].get('fields', None)
            }, 
            status=status.HTTP_200_OK
        )