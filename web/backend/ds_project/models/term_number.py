from django.db import models
from django.utils import timezone

class TermNumber(models.Model):
    term_number_id = models.AutoField(primary_key=True)
    term_number = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.term_number_id)