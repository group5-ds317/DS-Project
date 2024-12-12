from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from .faculty import Faculty
from .year import Year
from .term_number import TermNumber
from .course import Course

class SubjectScore(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, null=False, blank=False)
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=False, blank=False)
    year_id = models.ForeignKey(Year, on_delete=models.CASCADE, null=False, blank=False)
    term_number_id = models.ForeignKey(TermNumber, on_delete=models.CASCADE, null=False, blank=False)
    score = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0), MaxValueValidator(10)]),
    score_ratio = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0), MaxValueValidator(1)]),
    score_ratio_scaled = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0), MaxValueValidator(1)]),
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['course_id', 'year_id', 'faculty_id', 'term_number_id'],
                name='subject_score_primary_key'
            )
        ]
    
    def __str__(self):
        return str(self.course_id)