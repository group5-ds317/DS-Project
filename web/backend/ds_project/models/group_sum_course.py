from django.db import models
from django.utils import timezone
from .faculty import Faculty
from .year import Year
from .term_number import TermNumber

class GroupSumCourse(models.Model):
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=False, blank=False)
    year_id = models.ForeignKey(Year, on_delete=models.CASCADE, null=False, blank=False)
    term_number_id = models.ForeignKey(TermNumber, on_delete=models.CASCADE, null=False, blank=False)
    course_number = models.PositiveIntegerField(null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['faculty_id', 'year_id', 'term_number_id'],
                name='group_sum_course_primary_key'
            )
        ]
    
    def __str__(self):
        return str(self.faculty_id)