from django.urls import path
from ..views.import_data import ImportMajorData, ImportFacultyData, ImportTrainingSystemData, ImportGroupCourseTypeData, ImportCourseTypeData, ImportYearData, ImportTermData, ImportTermNumberData, ImportCourseData, ImportStudentData, ImportScoreData, ImportGroupCourseData, ImportGroupSumCourseData, ImportSubjectPopularityData, ImportSubjectScoreData


urlpatterns = [
    path('import-major', ImportMajorData.as_view(), name='import-major'),
    path('import-faculty', ImportFacultyData.as_view(), name='import-faculty'),
    path('import-training-system', ImportTrainingSystemData.as_view(), name='import-training-system'),
    path('import-group-course-type', ImportGroupCourseTypeData.as_view(), name='import-group-course-type'),
    path('import-course-type', ImportCourseTypeData.as_view(), name='import-course-type'),
    path('import-year', ImportYearData.as_view(), name='import-year'),
    path('import-term', ImportTermData.as_view(), name='import-term'),
    path('import-term-number', ImportTermNumberData.as_view(), name='import-term-number'),
    path('import-course', ImportCourseData.as_view(), name='import-course'),
    path('import-student', ImportStudentData.as_view(), name='import-student'),
    path('import-score', ImportScoreData.as_view(), name='import-score'),
    path('import-group-course', ImportGroupCourseData.as_view(), name='import-group-course'),
    path('import-group-sum-course', ImportGroupSumCourseData.as_view(), name='import-group-sum-course'),
    path('import-subject-popularity', ImportSubjectPopularityData.as_view(), name='import-subject-popularity'),
    path('import-subject-score', ImportSubjectScoreData.as_view(), name='import-subject-score'),

]