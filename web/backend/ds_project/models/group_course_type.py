from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator

class GroupCourseType(models.Model):
    group_course_type_id = models.AutoField(primary_key=True)
    group_course_type = models.TextField(max_length=255, null=False, blank=False, validators=[MinLengthValidator(1)])
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.group_course_type_id)