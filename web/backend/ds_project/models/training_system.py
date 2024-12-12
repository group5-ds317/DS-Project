from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator

class TrainingSystem(models.Model):
    training_system_id = models.AutoField(primary_key=True)
    training_system = models.TextField(max_length=255, null=False, blank=False, validators=[MinLengthValidator(1)])
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.training_system_id)