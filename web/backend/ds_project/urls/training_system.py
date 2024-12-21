from django.urls import path
from ..views.training_system import GetTrainingSystemAPIView

urlpatterns = [
    path('get-training-system', GetTrainingSystemAPIView.as_view(), name='get-training-system'),
]