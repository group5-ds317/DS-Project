import numpy as np
import pandas as pd
import math
from django.db.models import Avg, Q
from sklearn.preprocessing import normalize
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from ..models.student import Student
from ..models.faculty import Faculty
from ..models.major import Major
from ..models.training_system import TrainingSystem
from ..models.score import Score
from ..models.year import Year
from ..models.term import Term
from ..models.term_number import TermNumber
from ..models.course import Course
from ..models.course_type import CourseType
from ..models.group_course_type import GroupCourseType
from ..models.subject_popularity import SubjectPopularity
from ..models.group_sum_course import GroupSumCourse

class MainBaseline():
    def get_group_sum_course(self, faculty: str, year: int, term: int):
    #   group_course_result = self.group_sum_course.loc[(self.group_sum_course['faculty'] == faculty) & (self.group_sum_course['year'] < year) & (self.group_sum_course['term_number'] == term - 1), :]
    #   group_course_result = group_course_result[['faculty', 'course_number']]
    #   group_course_result = group_course_result.groupby('faculty').mean()
    #   group_course_result['course_number'] = group_course_result['course_number'].apply(lambda x: math.ceil(x))
    #   group_course_result = group_course_result.reset_index()
    #   return group_course_result.iloc[0]['course_number']
        faculty_id = Faculty.objects.get(faculty=faculty).faculty_id
        year_list = [y for y in range(2013, year)] if year > 2013 else []
        year_ids = [Year.objects.get(year=y).year_id for y in year_list]
        term_number_id = TermNumber.objects.get(term_number=term-1).term_number_id
        group_course_result = GroupSumCourse.objects.filter(
            faculty_id=faculty_id,
            year_id__in=year_ids,
            term_number_id=term_number_id
        )
        group_course_result = group_course_result.aggregate(Avg('course_number'))
        group_course_result = group_course_result['course_number__avg']
        group_course_result = math.ceil(group_course_result)
        return group_course_result


    def get_subject_popularity(self, faculty: str, start_year: int, top_m: int, current_term: int, attended_courses: list[str]):
        # student_info = self.student[self.student['mssv'] == mssv].iloc[0]
        # faculty = student_info['faculty']
        # start_year = student_info['start_year']

        # target_year = start_year + (current_term - 1) // 2
        # target_term = (current_term - 1) % 2 + 1
        # faculty_courses = self.subject[self.subject['faculty'] == faculty]
        # previous_courses = faculty_courses[
        #     (faculty_courses['year'] < target_year) |
        #     ((faculty_courses['year'] == target_year) & (faculty_courses['term_number'] < target_term))
        # ]
        # previous_courses = previous_courses.sort_values(by=['popularity_scaled'], ascending=False)
        # previous_courses = previous_courses.drop_duplicates(subset=['course_id'], keep='first')
        # previous_courses = previous_courses[~previous_courses['course_id'].isin(attended_courses)]
        # top_courses = previous_courses.nlargest(top_m, 'student_number')['course_id']
        # return top_courses.values
        target_year = start_year + (current_term - 1) // 2
        target_year_id = Year.objects.get(year=target_year).year_id
        before_target_year_list = [y for y in range(2013, target_year)] if target_year > 2013 else []
        before_target_year_ids = [Year.objects.get(year=y).year_id for y in before_target_year_list]
        target_term = (current_term - 1) % 2 + 1
        before_target_term_list = [t for t in range(1, target_term)] if target_term > 1 else []
        before_target_term_ids = [TermNumber.objects.get(term_number=t).term_number_id for t in before_target_term_list]
        faculty_courses = SubjectPopularity.objects.filter(faculty_id__faculty=faculty)
        previous_courses = faculty_courses.filter(
           Q(year_id__in=before_target_year_ids) |
           (Q(year_id=target_year_id) & Q(term_number_id__in=before_target_term_ids))
        )
        previous_courses = previous_courses.order_by('-popularity_scaled')
        previous_courses = previous_courses.values('course_id').distinct()
        previous_courses = previous_courses.exclude(course_id__in=attended_courses)
        top_courses = previous_courses.order_by('-student_number')[:top_m]
        top_courses_list = top_courses.values_list('course_id', flat=True)
        return np.array(top_courses_list)


    def get_failed_courses(self, mssv: str, term: int):
        # failed_courses = self.score[
        #     (self.score['mssv'] == mssv) &
        #     (self.score['score'] < 5) &
        #     (self.score['term_number'] == term - 1)
        # ]['course_id'].unique()
        # return failed_courses
        term_number_id = TermNumber.objects.get(term_number=term - 1)
        failed_courses = Score.objects.filter(
           mssv=mssv,
           score__lt=5,
           term_number_id=term_number_id
        )
        failed_courses = failed_courses.values('course_id').distinct()
        failed_courses_list = failed_courses.values_list('course_id', flat=True) 
        return np.array(failed_courses_list)

    def get_attended_courses(self, mssv: str, term: int):
        # attended_courses = self.score[
        #     (self.score['mssv'] == mssv) &
        #     (self.score['term_number'] == term - 1)
        # ]['course_id'].unique()
        # return attended_courses
        term_number_id = TermNumber.objects.get(term_number=term - 1)
        attended_courses = Score.objects.filter(
           mssv=mssv,
           term_number_id=term_number_id
        )
        attended_courses = attended_courses.values('course_id').distinct()
        attended_courses_list = attended_courses.values_list('course_id', flat=True)
        return np.array(attended_courses_list)

    def get_all_attended_courses(self, mssv: str, term: int):
        # attended_courses = self.score[
        #     (self.score['mssv'] == mssv) &
        #     (self.score['term_number'] < term)
        # ]['course_id'].unique()
        # return attended_courses
        term_number_ids = TermNumber.objects.filter(term_number__lt=term)
        attended_courses = Score.objects.filter(
           mssv=mssv,
           term_number_id__in=term_number_ids
        )
        attended_courses = attended_courses.values('course_id').distinct()
        attended_courses_list = attended_courses.values_list('course_id', flat=True)
        return np.array(attended_courses_list)

    def combined_feature(self, courses: np.array) -> list:
        # course_texts = self.course[self.course['course_id'].isin(courses)].apply(
        #     lambda row: f"{row['course_id']} {row['major']} {row['course_type']} {row['group_course_type']}", axis=1
        # ).tolist()
        # return course_texts
        selected_courses = Course.objects.filter(
           course_id__in=courses
        )
        selected_courses_text = [
           f"{course.course_id} {course.major_id.major} {course.course_type_id.course_type} {course.group_course_type_id.group_course_type}"
           for course in selected_courses
        ]
        return selected_courses_text

    def aggregate_cosine_sim(self, cosine_sim_matrix: pd.DataFrame, type: str) -> pd.DataFrame:
      if type == 'max':
        return cosine_sim_matrix.max(axis=1)
      elif type == 'min':
        return cosine_sim_matrix.min(axis=1)
      elif type == 'mean':
        return cosine_sim_matrix.mean(axis=1)
      elif type == 'sum':
        return cosine_sim_matrix.sum(axis=1)


    def recommend(self, mssv: str, term: int, pooling: str, top_m: int) -> pd.DataFrame:
        faculty = Student.objects.get(mssv=mssv).faculty_id.faculty
        # faculty = faculty.strip()
        # year = int(self.score[(self.score['mssv'] == mssv) & (self.score['term_number'] == term)]['year'].iloc[0])
        year = Score.objects.filter(mssv=mssv, term_number_id__term_number=term).first().year_id.year
        start_year = Student.objects.get(mssv=mssv).start_year

        all_attended_courses = self.get_all_attended_courses(mssv, term)
        attended_courses = self.get_attended_courses(mssv, term)
        failed_courses = self.get_failed_courses(mssv, term)

        popular_courses = self.get_subject_popularity(faculty, start_year,top_m, term, all_attended_courses)

        recommended_courses = np.setdiff1d(popular_courses, all_attended_courses)
        recommended_courses = np.unique(np.concatenate((recommended_courses, failed_courses)))

        all_courses = np.concatenate((attended_courses, recommended_courses))
        course_texts = self.combined_feature(all_courses)

        vectorizer = TfidfVectorizer()
        vectorizer.fit(course_texts)

        attended_vectors = vectorizer.transform(self.combined_feature(attended_courses))
        recommended_vectors = vectorizer.transform(self.combined_feature(recommended_courses))

        cosine_sim_matrix = cosine_similarity(recommended_vectors, attended_vectors)
        cosine_sim_matrix_df = pd.DataFrame(cosine_sim_matrix, index=recommended_courses, columns=attended_courses)

        top_n = self.get_group_sum_course(faculty, year, term)
        pooling_cosine = self.aggregate_cosine_sim(cosine_sim_matrix_df, pooling)
        max_cosine = self.aggregate_cosine_sim(cosine_sim_matrix_df, 'max')
        top_recommended_pooling_cosine = pooling_cosine.nlargest(int(top_n)).reset_index().rename(columns={'index': 'course_id', 0: 'similarity_score'})
        top_recommended_max_cosine = max_cosine.reset_index().rename(columns={'index': 'course_id', 0: 'similarity_score'})
        top_recommended_max_cosine = top_recommended_max_cosine[top_recommended_max_cosine['course_id'].isin(top_recommended_pooling_cosine['course_id'])]

        return top_recommended_pooling_cosine, top_recommended_max_cosine

