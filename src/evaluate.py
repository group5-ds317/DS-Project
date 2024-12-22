from tqdm import tqdm
import numpy as np
import pandas as pd
import math
from .model import Model
processed_student = pd.read_excel('/content/drive/MyDrive/Nhóm 5 - DS317.P11/Đồ án mô học/Dataset/Processed/Processed Data With Raw Data/processed_student.xlsx', index_col=0)
processed_course = pd.read_excel('/content/drive/MyDrive/Nhóm 5 - DS317.P11/Đồ án mô học/Dataset/Processed/Processed Data With Raw Data/processed_course.xlsx', index_col=0)
processed_score = pd.read_excel('/content/drive/MyDrive/Nhóm 5 - DS317.P11/Đồ án mô học/Dataset/Processed/Processed Data With Raw Data/processed_score.xlsx', index_col=0)
subject_popularity = pd.read_excel('/content/drive/MyDrive/Nhóm 5 - DS317.P11/Đồ án mô học/Dataset/Processed/Processed Data With Raw Data/subject_popularity.xlsx', index_col = 0)
group_sum_course = pd.read_excel('/content/drive/MyDrive/Nhóm 5 - DS317.P11/Đồ án mô học/Dataset/Processed/Processed Data With Raw Data/group_sum_course.xlsx')


# Lọc các sinh viên bắt đầu học năm 2014
student_2014 = processed_student[processed_student['namhoc_batdau'] == 2014]['mssv'].unique()

terms = [2, 3, 4, 5]
filtered_scores = processed_score[processed_score['sohocky'].isin(terms) & processed_score['mssv'].isin(student_2014)]

student_with_all_terms = filtered_scores.groupby('mssv').filter(lambda x: set(x['sohocky']) == set(terms))['mssv'].unique()

student_with_all_terms = list(student_with_all_terms)


qualified_students = list(set(student_2014) & set(student_with_all_terms))
# selected_students = random.sample(qualified_students, 100)

gridsearch_results = []
for pooling in tqdm(['max', 'min', 'mean', 'sum']):
  for m in range(1, 21):
    evaluation_results = []
    for i in range(2, 6):
      for mssv in qualified_students:
          pipeline = Model(processed_student, processed_score, processed_course, subject_popularity, group_sum_course)
          precision, recall, f1_score = pipeline.evaluate(mssv, i, pooling, m)
          evaluation_results.append({
              'mssv': mssv,
              'term': i,
              'precision': precision,
              'recall': recall,
              'f1_score': f1_score
          })

    evaluation_df = pd.DataFrame(evaluation_results)
    mean_precision_by_term = evaluation_df.groupby('term')['precision'].mean()
    mean_precision = evaluation_df['precision'].mean()
    mean_recall_by_term = evaluation_df.groupby('term')['recall'].mean()
    mean_recall = evaluation_df['recall'].mean()
    mean_f1_score_by_term = evaluation_df.groupby('term')['f1_score'].mean()
    mean_f1_score = evaluation_df['f1_score'].mean()
    gridsearch_results.append({
        'pooling': pooling,
        'm': m,
        'mean_precision': mean_precision,
        'mean_recall': mean_recall,
        'mean_f1_score': mean_f1_score
    })
gridsearch_df = pd.DataFrame(gridsearch_results)