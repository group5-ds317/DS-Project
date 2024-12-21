from django.urls import path
from ..views.course import GetCourseAPIView

urlpatterns = [
    path('get-course', GetCourseAPIView.as_view(), name='get-course'),
]