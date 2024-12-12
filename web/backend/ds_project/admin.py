from django.contrib import admin
from .models import student, major, faculty, training_system, year, term, term_number, course_type, group_course_type, course, score, group_course, group_sum_course, subject_popularity, subject_score, phobert_paraphased_tomtat

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('mssv', 'gender', 'start_year', 'faculty_id', 'training_system_id', 'major_id', 'created_at', 'updated_at')
    list_filter = ['gender', 'start_year', 'created_at', 'updated_at']
    search_fields = ['mssv', 'faculty_id', 'training_system_id', 'major_id']

class MajorAdmin(admin.ModelAdmin):
    list_display = ('major_id', 'major', 'created_at', 'updated_at')
    list_filter = ['created_at', 'updated_at']
    search_fields = ['major_id', 'major']

class FacultyAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'faculty', 'created_at', 'updated_at')
    list_filter = ['created_at', 'updated_at']
    search_fields = ['faculty_id', 'faculty']

class TrainingSystemAdmin(admin.ModelAdmin):
    list_display = ('training_system_id', 'training_system', 'created_at', 'updated_at')
    list_filter = ['created_at', 'updated_at']
    search_fields = ['training_system_id', 'training_system']

class YearAdmin(admin.ModelAdmin):
    list_display = ('year_id', 'year', 'created_at', 'updated_at')
    list_filter = ['created_at', 'updated_at']
    search_fields = ['year_id', 'year']

class TermAdmin(admin.ModelAdmin):
    list_display = ('term_id', 'term', 'created_at', 'updated_at')
    list_filter = ['created_at', 'updated_at']
    search_fields = ['term_id', 'term']

class TermNumberAdmin(admin.ModelAdmin):
    list_display = ('term_number_id', 'term_number', 'created_at', 'updated_at')
    list_filter = ['created_at', 'updated_at']
    search_fields = ['term_number_id', 'term_number']

class CourseTypeAdmin(admin.ModelAdmin):
    list_display = ('course_type_id', 'course_type', 'group_course_type_id', 'created_at', 'updated_at')
    list_filter = ['created_at', 'updated_at']
    search_fields = ['course_type_id', 'course_type', 'group_course_type_id']

class GroupCourseTypeAdmin(admin.ModelAdmin):
    list_display = ('group_course_type_id', 'group_course_type', 'created_at', 'updated_at')
    list_filter = ['created_at', 'updated_at']
    search_fields = ['group_course_type_id', 'group_course_type']

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'credit', 'major_id', 'course_type_id', 'group_course_type_id', 'created_at', 'updated_at')
    list_filter = ['created_at', 'updated_at']
    search_fields = ['course_id', 'credit', 'major_id', 'course_type_id', 'group_course_type_id']

class ScoreAdmin(admin.ModelAdmin):
    list_display = ('mssv', 'course_id', 'term_number_id', 'year_id', 'term_id', 'score', 'status', 'passed', 'created_at', 'updated_at')
    list_filter = ['status', 'passed', 'created_at', 'updated_at']
    search_fields = ['mssv', 'course_id', 'term_number_id', 'year_id', 'term_id', 'score']

class GroupCourseAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'term_number_id', 'year_id', 'group_course_type_id', 'course_number', 'created_at', 'updated_at')
    list_filter = ['created_at', 'updated_at']
    search_fields = ['faculty_id', 'term_number_id', 'year_id', 'group_course_type_id', 'course_number']

class GroupSumCourseAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'term_number_id', 'year_id', 'course_number', 'created_at', 'updated_at')
    list_filter = ['created_at', 'updated_at']
    search_fields = ['faculty_id', 'term_number_id', 'year_id', 'course_number']

class SubjectPopularityAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'term_number_id', 'year_id', 'course_id', 'student_number', 'total_student_number', 'popularity', 'popularity_scaled', 'created_at', 'updated_at')
    list_filter = ['created_at', 'updated_at']
    search_fields = ['faculty_id', 'term_number_id', 'year_id', 'course_id', 'student_number', 'total_student_number', 'popularity', 'popularity_scaled']

class SubjectScoreAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'term_number_id', 'year_id', 'course_id', 'score', 'score_ratio', 'score_ratio_scaled', 'created_at', 'updated_at')
    list_filter = ['created_at', 'updated_at']
    search_fields = ['faculty_id', 'term_number_id', 'year_id', 'course_id', 'score', 'score_ratio', 'score_ratio_scaled']
    
class PhoBERTParaphasedTomtatAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'created_at', 'updated_at') + tuple([f'embedding_dim_{i}'for i in range(768)])
    list_filter = ['created_at', 'updated_at']
    search_fields = ['course_id']

admin.site.register(student.Student, StudentAdmin)
admin.site.register(major.Major, MajorAdmin)
admin.site.register(faculty.Faculty, FacultyAdmin)
admin.site.register(training_system.TrainingSystem, TrainingSystemAdmin)
admin.site.register(term.Term, TermAdmin)
admin.site.register(year.Year, YearAdmin)
admin.site.register(term_number.TermNumber, TermNumberAdmin)
admin.site.register(course_type.CourseType, CourseTypeAdmin)
admin.site.register(group_course_type.GroupCourseType, GroupCourseTypeAdmin)
admin.site.register(course.Course, CourseAdmin)
admin.site.register(score.Score, ScoreAdmin)
admin.site.register(group_course.GroupCourse, GroupCourseAdmin)
admin.site.register(group_sum_course.GroupSumCourse, GroupSumCourseAdmin)
admin.site.register(subject_popularity.SubjectPopularity, SubjectPopularityAdmin)
admin.site.register(subject_score.SubjectScore, SubjectScoreAdmin)
admin.site.register(phobert_paraphased_tomtat.PhoBERTParaphasedTomtat, PhoBERTParaphasedTomtatAdmin)