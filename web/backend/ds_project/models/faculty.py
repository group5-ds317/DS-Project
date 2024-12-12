from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator

class Faculty(models.Model):
    faculty_id = models.AutoField(primary_key=True)
    faculty = models.TextField(max_length=255, null=False, blank=False, validators=[MinLengthValidator(1)])
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.faculty_id)