from django.urls import path
from ..views.student import LoginAPIView, LogoutAPIView, GetStudentAPIView, GetAttendedCourseAPIView, GetUnAttendedCourseAPIView, GetRecommendedCourseAPIView

urlpatterns = [
    path('login', LoginAPIView.as_view(), name='login'),
    path('logout', LogoutAPIView.as_view(), name='logout'),
    path('get-student', GetStudentAPIView.as_view(), name='get-student'),
    path('get-attended-course', GetAttendedCourseAPIView.as_view(), name='get-attended-course'),
    path('get-unattended-course', GetUnAttendedCourseAPIView.as_view(), name='get-unattended-course'),
    path('get-recommended-course', GetRecommendedCourseAPIView.as_view(), name='get-recommended-course'),

]