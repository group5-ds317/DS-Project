from django.db import models
from django.utils import timezone
from .major import Major
from .group_course_type import GroupCourseType
from .course_type import CourseType

class Course(models.Model):
    course_id = models.TextField(primary_key=True)
    course_name = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    credit = models.PositiveIntegerField(null=False, blank=False)
    major_id = models.ForeignKey(Major, on_delete=models.CASCADE, null=False, blank=False)
    course_type_id = models.ForeignKey(CourseType, on_delete=models.CASCADE, null=False, blank=False)
    group_course_type_id = models.ForeignKey(GroupCourseType, on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.course_id)