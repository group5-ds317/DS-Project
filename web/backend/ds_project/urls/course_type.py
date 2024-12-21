from django.urls import path
from ..views.course_type import GetCourseTypeAPIView

urlpatterns = [
    path('get-course-type', GetCourseTypeAPIView.as_view(), name='get-course-type'),
]