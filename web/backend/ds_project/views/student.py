from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from ..models.student import Student
from ..models.faculty import Faculty
from ..models.major import Major
from ..models.training_system import TrainingSystem
from ..models.score import Score
from ..models.term_number import TermNumber
from ..models.course import Course
from ..models.course_type import CourseType
from ..models.group_course_type import GroupCourseType
from ..models.subject_popularity import SubjectPopularity
from ..models.group_sum_course import GroupSumCourse
from django.utils import timezone
from django.core import serializers
from ..baseline.main_baseline import MainBaseline
import re
import copy
import json
# from django.contrib.auth.hashers import make_password, check_password

baseline = MainBaseline()
POOLING = 'min'
TOP_M = 8

class LoginAPIView(GenericAPIView):
    def post(self, request):
        data = request.data
        try:
            mssv = data['mssv']
            password = data['password']
        except:
            return Response(
                {
                    "success": False,
                    "message": "Thông tin sinh viên không hợp lệ"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        if not mssv or len(mssv) == 0:
            return Response(
                {
                    "success": False,
                    "message": "Mã số sinh viên không hợp lệ"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
    
        if not password or len(password) == 0 or not re.match(r"^\d{6}$", password):
            return Response(
                {
                    "success": False,
                    "message": "Mật khẩu không hợp lệ"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
      
        try:
            instance = Student.objects.get(mssv=mssv)
            if password != instance.password:
                return Response(
                    {
                        "success": False,
                        "message": "Mật khẩu không hợp lệ"
                    }, 
                    status=status.HTTP_401_UNAUTHORIZED
                )

            instance.login_at = timezone.now()
            instance.save()
            
        except Student.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Sinh viên không tồn tại"
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

        return Response(
            {
                "success": True,
                "message": "Đăng nhập thành công",
                "data": {
                    "mssv": instance.mssv
                }
            }, 
            status=status.HTTP_200_OK
        )
    
class LogoutAPIView(GenericAPIView):
    def post(self, request):
        data = request.data
        try:
            mssv = data['mssv']
        except:
            return Response(
                {
                    "success": False,
                    "message": "Thông tin sinh viên không hợp lệ"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        if not mssv or len(mssv) == 0:
            return Response(
                {
                    "success": False,
                    "message": "Mã sinh viên không hợp lệ"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            instance = Student.objects.get(mssv=mssv)
        except Student.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Sinh viên không tồn tại"
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
        
        return Response(
            {
                "success": True,
                "message": "Đăng xuất thành công"
            }, 
            status=status.HTTP_200_OK
        )
    
class GetStudentAPIView(GenericAPIView):
    def get(self, request):
        params = request.query_params
        try:
            mssv = params['mssv']
        except:
            return Response(
                {
                    "success": False,
                    "message": "Thông tin sinh viên không hợp lệ"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
     
        if not mssv or len(mssv) == 0:
            return Response(
                {
                    "success": False,
                    "message": "Mã sinh viên không hợp lệ"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
     
        try:
            instance = Student.objects.get(mssv=mssv)
        except Student.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Sinh viên không tồn tại"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except Faculty.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Khoa không tồn tại"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except Major.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Ngành học không tồn tại"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
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
        copy_instance.password = None
        json_data = json.loads(serializers.serialize('json', [copy_instance]))

        return Response(
            {
                "success": True,
                "message": "Truy xuất sinh viên thành công",
                "data": json_data[0].get('fields', None)
            }, 
            status=status.HTTP_200_OK
        )
    
class GetRecommendedCourseAPIView(GenericAPIView):
    def get(self, request):
        params = request.query_params
        try:
            mssv = params['mssv']
            term_number = int(params['term_number'])
        except:
            return Response(
                {
                    "success": False,
                    "message": "Thông tin sinh viên không hợp lệ"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
     
        if not mssv or len(mssv) == 0:
            return Response(
                {
                    "success": False,
                    "message": "Mã sinh viên không hợp lệ"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            _ = Student.objects.get(mssv=mssv)
        except Student.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Sinh viên không tồn tại"
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
        
        recommend_courses, max_cosine = baseline.recommend(mssv, term_number, POOLING, TOP_M)
        course_ids = recommend_courses['course_id']
        
        try:
            courses = [
                Course.objects.get(course_id=course_id)
                for course_id in course_ids
            ]
            course_data = []
            for course in courses:
                course_data.append({
                    'course_id': course.course_id,
                    'similarity_score': max_cosine[max_cosine['course_id'] == course.course_id]['similarity_score'],
                    'course_name': course.course_name,
                    'summary': course.summary,
                    'credit': course.credit,
                    'major': course.major_id.major,
                    'course_type': course.course_type_id.course_type,
                    'group_course_type': course.group_course_type_id.group_course_type,
                    'updated_at': course.updated_at,
                    'created_at': course.created_at
                })
        except Course.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Môn học không tồn tại"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except Major.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Ngành học không tồn tại"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except CourseType.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Loại môn học không tồn tại"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except GroupCourseType.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Nhóm loại môn học không tồn tại"
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

        return Response(
            {
                "success": True,
                "message": "Truy xuất môn học khuyến nghị thành công",
                "data": {
                    "courses": course_data
                }
            }, 
            status=status.HTTP_200_OK
        )
    
class GetAttendedCourseAPIView(GenericAPIView):
    def get(self, request):
        params = request.query_params
        try:
            mssv = params['mssv']
            term_number = int(params['term_number'])
        except:
            return Response(
                {
                    "success": False,
                    "message": "Thông tin sinh viên không hợp lệ"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
     
        if not mssv or len(mssv) == 0:
            return Response(
                {
                    "success": False,
                    "message": "Mã sinh viên không hợp lệ"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            _ = Student.objects.get(mssv=mssv)
            term_number_list = [i for i in range(1, term_number)] if term_number > 1 else []
            term_number_instances = [TermNumber.objects.get(term_number=single_term_number) for single_term_number in term_number_list]
            score_instances = [Score.objects.filter(mssv=mssv, term_number_id=term_number_instance) for term_number_instance in term_number_instances]
        except Student.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Sinh viên không tồn tại"
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
        
        course_ids = []
        for score_instance_set in score_instances:
            for score_instance in score_instance_set:
                course_ids.append(str(score_instance.course_id))

        course_ids = list(set(course_ids))

        try:
            courses = [
                Course.objects.get(course_id=course_id)
                for course_id in course_ids
            ]
            course_data = []
            for course in courses:
                course_data.append({
                    'course_id': course.course_id,
                    'course_name': course.course_name,
                    'summary': course.summary,
                    'credit': course.credit,
                    'major': course.major_id.major,
                    'course_type': course.course_type_id.course_type,
                    'group_course_type': course.group_course_type_id.group_course_type,
                    'updated_at': course.updated_at,
                    'created_at': course.created_at
                })
        except Course.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Môn học không tồn tại"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except Major.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Ngành học không tồn tại"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except CourseType.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Loại môn học không tồn tại"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except GroupCourseType.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Nhóm loại môn học không tồn tại"
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

        return Response(
            {
                "success": True,
                "message": "Truy xuất môn học đã đăng ký thành công",
                "data": {
                    "courses": course_data
                }
            }, 
            status=status.HTTP_200_OK
        )
    
class GetUnAttendedCourseAPIView(GenericAPIView):
    def get(self, request):
        params = request.query_params
        try:
            mssv = params['mssv']
            term_number = int(params['term_number'])
        except:
            return Response(
                {
                    "success": False,
                    "message": "Thông tin sinh viên không hợp lệ"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
     
        if not mssv or len(mssv) == 0:
            return Response(
                {
                    "success": False,
                    "message": "Mã sinh viên không hợp lệ"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            _ = Student.objects.get(mssv=mssv)
            all_course_instances = Course.objects.all()

            term_number_list = [i for i in range(1, term_number)] if term_number > 1 else []
            term_number_instances = [TermNumber.objects.get(term_number=single_term_number) for single_term_number in term_number_list]
            score_instances = [Score.objects.filter(mssv=mssv, term_number_id=term_number_instance) for term_number_instance in term_number_instances]
        except Student.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Sinh viên không tồn tại"
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
        
        all_course_ids = [course_instance.course_id for course_instance in all_course_instances]
        all_course_ids = set(all_course_ids)

        attended_course_ids = []
        for score_instance_set in score_instances:
            for score_instance in score_instance_set:
                attended_course_ids.append(str(score_instance.course_id))

        attended_course_ids = set(attended_course_ids)

        unattended_course_ids = list(all_course_ids.difference(attended_course_ids))

        try:
            courses = [
                Course.objects.get(course_id=course_id)
                for course_id in unattended_course_ids
            ]
            course_data = []
            for course in courses:
                course_data.append({
                    'course_id': course.course_id,
                    'course_name': course.course_name,
                    'summary': course.summary,
                    'credit': course.credit,
                    'major': course.major_id.major,
                    'course_type': course.course_type_id.course_type,
                    'group_course_type': course.group_course_type_id.group_course_type,
                    'updated_at': course.updated_at,
                    'created_at': course.created_at
                })
        except Course.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Môn học không tồn tại"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except Major.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Ngành học không tồn tại"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except CourseType.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Loại môn học không tồn tại"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except GroupCourseType.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": "Nhóm loại môn học không tồn tại"
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

        return Response(
            {
                "success": True,
                "message": "Truy xuất môn học chưa đăng ký thành công",
                "data": {
                    "courses": course_data 
                }
            }, 
            status=status.HTTP_200_OK
        )