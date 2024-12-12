from django.db import models
from django.utils import timezone

class Year(models.Model):
    year_id = models.AutoField(primary_key=True)
    year = models.PositiveIntegerField(null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.year_id)