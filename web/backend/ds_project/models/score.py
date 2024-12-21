from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from .student import Student
from .course import Course
from .year import Year
from .term import Term
from .term_number import TermNumber

class StatusChoices(models.IntegerChoices):
    HUY = 0, 'Hủy'
    BINHTHUONG = 1, 'Bình thường'
    TRANO = 2, 'Trả nợ'
    CAITHIEN = 3, 'Cải thiện'
    MIEN = 4, 'Miễn'
    HOAN = 5, 'Hoãn'

class PassedChoices(models.IntegerChoices):
    HOANTHANH = 1, 'Hoàn thành'
    KHONGHOANTHANH = 0, 'Không hoàn thành'

class Score(models.Model):
    mssv = models.ForeignKey(Student, on_delete=models.CASCADE, null=False, blank=False)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, null=False, blank=False)
    term_number_id = models.ForeignKey(TermNumber, on_delete=models.CASCADE, null=False, blank=False)
    year_id = models.ForeignKey(Year, on_delete=models.CASCADE, null=False, blank=False)
    term_id = models.ForeignKey(Term, on_delete=models.CASCADE, null=False, blank=False)
    score = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0)], default=0)
    status = models.IntegerField(choices=StatusChoices.choices, default=StatusChoices.BINHTHUONG)
    passed = models.IntegerField(choices=PassedChoices.choices, default=PassedChoices.HOANTHANH)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['mssv', 'course_id', 'year_id', 'term_id'],
                name='score_primary_key'
            )
        ]
     
    def __str__(self):
        return str(self.course_id)