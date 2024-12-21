from django.urls import path
from ..views.group_course_type import GetGroupCourseTypeAPIView

urlpatterns = [
    path('get-group-course-type', GetGroupCourseTypeAPIView.as_view(), name='get-group-course-type'),
]