from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from ..models.major import Major
from ..models.faculty import Faculty
from ..models.training_system import TrainingSystem
from ..models.group_course_type import GroupCourseType
from ..models.course_type import CourseType
from ..models.year import Year
from ..models.term import Term
from ..models.term_number import TermNumber
from ..models.course import Course
from ..models.student import Student
from ..models.score import Score
from ..models.group_course import GroupCourse
from ..models.group_sum_course import GroupSumCourse
from ..models.subject_popularity import SubjectPopularity
from ..models.subject_score import SubjectScore
from django.utils import timezone
import pandas as pd
import random

STUDENT_PATH = "D:/UIT/Courses/Data Analyst/Final Project/DS-Project/data/processed/processed data with pre-processed data/processed_student.xlsx"
COURSE_PATH = "D:/UIT/Courses/Data Analyst/Final Project/DS-Project/data/processed/processed data with pre-processed data/processed_course.xlsx"
SCORE_PATH = "D:/UIT/Courses/Data Analyst/Final Project/DS-Project/data/processed/processed data with pre-processed data/processed_score.xlsx"
TOMTAT_PATH = "D:/UIT/Courses/Data Analyst/Final Project/DS-Project/data/augmented/paraphrased_tomtat.xlsx"
GROUP_COURSE_PATH = "D:/UIT/Courses/Data Analyst/Final Project/DS-Project/data/processed/processed data with pre-processed data/group_course.xlsx"
GROUP_SUM_COURSE_PATH = "D:/UIT/Courses/Data Analyst/Final Project/DS-Project/data/processed/processed data with pre-processed data/group_sum_course.xlsx"
SUBJECT_POPULARITY_PATH = "D:/UIT/Courses/Data Analyst/Final Project/DS-Project/data/processed/processed data with pre-processed data/subject_popularity.xlsx"
SUBJECT_SCORE_PATH = "D:/UIT/Courses/Data Analyst/Final Project/DS-Project/data/processed/processed data with pre-processed data/subject_score.xlsx"
PHOBERT_PARAPHASED_TOMTAT = "D:/UIT/Courses/Data Analyst/Final Project/DS-Project/data/processed/processed data with pre-processed data/PhoBERT_paraphased_tomtat.csv"

class ImportMajorData(GenericAPIView):
    def post(self, request):
       
        course_df = pd.read_excel(COURSE_PATH)
        major_unique = course_df['nganhmh'].unique()
        for major in major_unique:
            if len(Major.objects.filter(major=major)) == 0: 
                new_major = Major(major=major)
                new_major.save()
        
        return Response(
            {
                "success": True,
                "message": "Nhập dữ liệu thành công",
            }, 
            status=status.HTTP_200_OK
        )
    
class ImportFacultyData(GenericAPIView):
    def post(self, request):
       
        student_df = pd.read_excel(STUDENT_PATH)
        faculty_unique = student_df['khoa'].unique()
        for faculty in faculty_unique:
            new_faculty = Faculty(faculty=faculty)
            new_faculty.save()
        
        return Response(
            {
                "success": True,
                "message": "Nhập dữ liệu thành công",
            }, 
            status=status.HTTP_200_OK
        )
    
class ImportTrainingSystemData(GenericAPIView):
    def post(self, request):
       
        student_df = pd.read_excel(STUDENT_PATH)
        training_system_unique = student_df['hedt'].unique()
        for training_system in training_system_unique:
            new_training_system = TrainingSystem(training_system=training_system)
            new_training_system.save()
        
        return Response(
            {
                "success": True,
                "message": "Nhập dữ liệu thành công",
            }, 
            status=status.HTTP_200_OK
        )

class ImportGroupCourseTypeData(GenericAPIView):
    def post(self, request):
       
        course_df = pd.read_excel(COURSE_PATH)
        group_course_type_unique = course_df['nhomloaimh'].unique()
        for group_course_type in group_course_type_unique:
            new_group_course_type = GroupCourseType(group_course_type=group_course_type)
            new_group_course_type.save()
        
        return Response(
            {
                "success": True,
                "message": "Nhập dữ liệu thành công",
            }, 
            status=status.HTTP_200_OK
        )
    
class ImportCourseTypeData(GenericAPIView):
    def post(self, request):
       
        course_df = pd.read_excel(COURSE_PATH)
        course_type_unique = course_df.groupby(['nhomloaimh'])['loaimh'].unique()
        for group_course_type, course_types in course_type_unique.items():
            group_course_type = GroupCourseType.objects.get(group_course_type=group_course_type)
            for course_type in course_types:
                new_course_type = CourseType(course_type=course_type, group_course_type_id=group_course_type)
                new_course_type.save()
        
        return Response(
            {
                "success": True,
                "message": "Nhập dữ liệu thành công",
            }, 
            status=status.HTTP_200_OK
        )
    
class ImportYearData(GenericAPIView):
    def post(self, request):
       
        score_df = pd.read_excel(SCORE_PATH)
        year_unique = score_df['namhoc'].unique()
        for year in year_unique:
            new_year = Year(year=year)
            new_year.save()
        
        return Response(
            {
                "success": True,
                "message": "Nhập dữ liệu thành công",
            }, 
            status=status.HTTP_200_OK
        )
    
class ImportTermData(GenericAPIView):
    def post(self, request):
       
        score_df = pd.read_excel(SCORE_PATH)
        term_unique = score_df['hocky'].unique()
        for term in term_unique:
            new_term = Term(term=term)
            new_term.save()
        
        return Response(
            {
                "success": True,
                "message": "Nhập dữ liệu thành công",
            }, 
            status=status.HTTP_200_OK
        )
    
class ImportTermNumberData(GenericAPIView):
    def post(self, request):
       
        score_df = pd.read_excel(SCORE_PATH)
        term_number_unique = score_df['sohocky'].unique()
        for term_number in term_number_unique:
            new_term_number = TermNumber(term_number=term_number)
            new_term_number.save()
        
        return Response(
            {
                "success": True,
                "message": "Nhập dữ liệu thành công",
            }, 
            status=status.HTTP_200_OK
        )
    
class ImportCourseData(GenericAPIView):
    def post(self, request):
       
        course_df = pd.read_excel(COURSE_PATH)
        tomtat_df = pd.read_excel(TOMTAT_PATH)
        for course in course_df.iterrows():
            course_name = tomtat_df.loc[tomtat_df['mamh'] == course[1]['mamh'], 'tenmh']
            course_name = course_name.iloc[0] if len(course_name) > 0 else ''
            summary = tomtat_df.loc[tomtat_df['mamh'] == course[1]['mamh'], 'tomtat']
            summary = summary.iloc[0] if len(summary) > 0 else ''
            major = Major.objects.get(major=course[1]['nganhmh'])
            course_type = CourseType.objects.get(course_type=course[1]['loaimh'])
            group_course_type = GroupCourseType.objects.get(group_course_type=course[1]['nhomloaimh'])
            new_course = Course(
                course_id=course[1]['mamh'],
                course_name=course_name,
                credit=course[1]['sotc'],
                major_id=major,
                course_type_id=course_type,
                group_course_type_id=group_course_type,
                summary=summary
            )
            new_course.save()
        
        return Response(
            {
                "success": True,
                "message": "Nhập dữ liệu thành công",
            }, 
            status=status.HTTP_200_OK
        )

class ImportStudentData(GenericAPIView):
    def post(self, request):
       
        student_df = pd.read_excel(STUDENT_PATH)
        passwords = set()
        for student in student_df.iterrows():
            if len(Student.objects.filter(mssv=student[1]['mssv'])) == 0: 
                new_password = random.randint(100000, 999999)
                while (new_password in passwords) and (len(Student.objects.filter(password=new_password)) > 0):
                    new_password = random.randint(100000, 999999)
                passwords.add(new_password)
                new_student = Student(
                    mssv=student[1]['mssv'],
                    gender=int(student[1]['gioitinh']),
                    start_year=int(student[1]['namhoc_batdau']),
                    faculty_id=Faculty.objects.get(faculty=student[1]['khoa']),
                    major_id=Major.objects.get(major=student[1]['nganhhoc']),
                    training_system_id=TrainingSystem.objects.get(training_system=student[1]['hedt']),
                    password=new_password
                )
                new_student.save()
        
        return Response(
            {
                "success": True,
                "message": "Nhập dữ liệu thành công",
            }, 
            status=status.HTTP_200_OK
        )
    
class ImportScoreData(GenericAPIView):
    def post(self, request):
       
        score_df = pd.read_excel(SCORE_PATH)
        for score in score_df.iterrows():
            new_score = Score(
                mssv=Student.objects.get(mssv=score[1]['mssv']),
                course_id=Course.objects.get(course_id=score[1]['mamh']),
                term_number_id=TermNumber.objects.get(term_number=score[1]['sohocky']),
                year_id=Year.objects.get(year=score[1]['namhoc']),
                term_id=Term.objects.get(term=score[1]['hocky']),
                score=score[1]['diem'],
                status=int(score[1]['trangthai']),
                passed=int(score[1]['hoanthanh'])
            )
            new_score.save()
        
        return Response(
            {
                "success": True,
                "message": "Nhập dữ liệu thành công",
            }, 
            status=status.HTTP_200_OK
        )
    
class ImportGroupCourseData(GenericAPIView):
    def post(self, request):
       
        group_course_df = pd.read_excel(GROUP_COURSE_PATH)
        for group_course in group_course_df.iterrows():
            new_group_course = GroupCourse(
                faculty_id=Faculty.objects.get(faculty=group_course[1]['khoa']),
                year_id=Year.objects.get(year=group_course[1]['namhoc']),
                term_number_id=TermNumber.objects.get(term_number=group_course[1]['sohocky']),
                group_course_type_id=GroupCourseType.objects.get(group_course_type=group_course[1]['nhomloaimh']),
                course_number=group_course[1]['somonhoc']
            )
            new_group_course.save()
        
        return Response(
            {
                "success": True,
                "message": "Nhập dữ liệu thành công",
            }, 
            status=status.HTTP_200_OK
        )
    
class ImportGroupSumCourseData(GenericAPIView):
    def post(self, request):
       
        group_sum_course_df = pd.read_excel(GROUP_SUM_COURSE_PATH)
        for group_sum_course in group_sum_course_df.iterrows():
            new_group_sum_course = GroupSumCourse(
                faculty_id=Faculty.objects.get(faculty=group_sum_course[1]['khoa']),
                year_id=Year.objects.get(year=group_sum_course[1]['namhoc']),
                term_number_id=TermNumber.objects.get(term_number=group_sum_course[1]['sohocky']),
                course_number=group_sum_course[1]['somonhoc']
            )
            new_group_sum_course.save()
        
        return Response(
            {
                "success": True,
                "message": "Nhập dữ liệu thành công",
            }, 
            status=status.HTTP_200_OK
        )

class ImportSubjectPopularityData(GenericAPIView):
    def post(self, request):
       
        subject_popularity_df = pd.read_excel(SUBJECT_POPULARITY_PATH)
        for subject_popularity in subject_popularity_df.iterrows():
            new_subject_popularity = SubjectPopularity(
                course_id=Course.objects.get(course_id=subject_popularity[1]['mamh']),
                faculty_id=Faculty.objects.get(faculty=subject_popularity[1]['khoa']),
                year_id=Year.objects.get(year=subject_popularity[1]['namhoc']),
                term_number_id=TermNumber.objects.get(term_number=subject_popularity[1]['sohocky']),
                student_number=int(subject_popularity[1]['sosv']),
                total_student_number=int(subject_popularity[1]['tongsosv']),
                popularity=float(subject_popularity[1]['dophobien']),
                popularity_scaled=float(subject_popularity[1]['dophobien_scaled'])
            )
            new_subject_popularity.save()
        
        return Response(
            {
                "success": True,
                "message": "Nhập dữ liệu thành công",
            }, 
            status=status.HTTP_200_OK
        )
    
class ImportSubjectScoreData(GenericAPIView):
    def post(self, request):
       
        subject_score_df = pd.read_excel(SUBJECT_SCORE_PATH)
        for subject_score in subject_score_df.iterrows():
            new_subject_score = SubjectScore(
                course_id=Course.objects.get(course_id=subject_score[1]['mamh']),
                faculty_id=Faculty.objects.get(faculty=subject_score[1]['khoa']),
                year_id=Year.objects.get(year=subject_score[1]['namhoc']),
                term_number_id=TermNumber.objects.get(term_number=subject_score[1]['sohocky']),
                score=float(subject_score[1]['diemtb']),
                score_ratio=float(subject_score[1]['dothanhtich']),
                score_ratio_scaled=float(subject_score[1]['dothanhtich_scaled'])
            )
            new_subject_score.save()
        
        return Response(
            {
                "success": True,
                "message": "Nhập dữ liệu thành công",
            }, 
            status=status.HTTP_200_OK
        )