from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator
from .group_course_type import GroupCourseType

class CourseType(models.Model):
    course_type_id = models.AutoField(primary_key=True)
    course_type = models.TextField(max_length=255, null=False, blank=False, validators=[MinLengthValidator(1)])
    group_course_type_id = models.ForeignKey(GroupCourseType, on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.course_type_id)