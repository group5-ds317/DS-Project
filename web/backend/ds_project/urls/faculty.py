from django.urls import path
from ..views.faculty import GetFacultyAPIView

urlpatterns = [
    path('get-faculty', GetFacultyAPIView.as_view(), name='get-faculty'),
]