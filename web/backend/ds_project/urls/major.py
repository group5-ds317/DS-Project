from django.urls import path
from ..views.major import GetMajorAPIView

urlpatterns = [
    path('get-major', GetMajorAPIView.as_view(), name='get-major'),
]