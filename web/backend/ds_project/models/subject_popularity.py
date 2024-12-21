from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from .faculty import Faculty
from .year import Year
from .term_number import TermNumber
from .course import Course

class SubjectPopularity(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, null=False, blank=False)
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=False, blank=False)
    year_id = models.ForeignKey(Year, on_delete=models.CASCADE, null=False, blank=False)
    term_number_id = models.ForeignKey(TermNumber, on_delete=models.CASCADE, null=False, blank=False)
    student_number = models.PositiveIntegerField(null=False, blank=False)
    total_student_number = models.PositiveIntegerField(null=False, blank=False)
    popularity = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0)], default=0)
    popularity_scaled = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0)], default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['course_id', 'year_id', 'faculty_id', 'term_number_id'],
                name='subject_popularity_primary_key'
            )
        ]
    
    def __str__(self):
        return str(self.course_id)