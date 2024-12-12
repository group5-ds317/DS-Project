from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator
from .faculty import Faculty
from .major import Major
from .training_system import TrainingSystem

class Gender(models.IntegerChoices):
    MALE = 1, 'Male'
    FEMALE = 0, 'Female'

class Student(models.Model):
    mssv = models.TextField(primary_key=True, null=False, blank=False, validators=[MinLengthValidator(1)])
    gender = models.IntegerField(choices=Gender.choices, default=Gender.MALE)
    start_year = models.PositiveIntegerField(null=False, blank=False)
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=False, blank=False)
    major_id = models.ForeignKey(Major, on_delete=models.CASCADE, null=False, blank=False)
    training_system_id = models.ForeignKey(TrainingSystem, on_delete=models.CASCADE, null=False, blank=False)
    password = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.mssv)