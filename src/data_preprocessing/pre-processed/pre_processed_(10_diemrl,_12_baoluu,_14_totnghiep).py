# -*- coding: utf-8 -*-
"""Pre-processed (10.diemrl, 12.baoluu, 14.totnghiep).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-jO4omEX4Qt82y4Rwc40CWAyvgyK9RH7
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
from fuzzywuzzy import fuzz, process
import math
import os

file_path1 = os.path.join('..', 'Education_dataset_V2', '10.diemrl.xlsx')
file_path2 = os.path.join('..', 'Education_dataset_V2', '12.baoluu.xlsx')
file_path3 = os.path.join('..', 'Education_dataset_V2', '14.totnghiep.xlsx')

drl_df = pd.read_excel(file_path1)
bl_df = pd.read_excel(file_path2)
tn_df = pd.read_excel(file_path3)

"""# ** 10.diemrl **"""

# Xác định các cột dữ liệu
drl_df.columns = drl_df.columns.str.strip() # xóa bỏ khoảng trắng thừa trong tên các cột
drl_cols = drl_df.columns.to_list()
drl_df.head()

drl_df.dtypes

# Tìm kiếm và xóa bỏ các dòng giá trị trống
drl_df.isnull().sum()

drl_df = drl_df.dropna(how='all')
drl_df.isnull().sum()

drl_cols

# Xác định các trường dữ liệu liên tục và rời rạc
drl_continuous_feature = ['drl']
drl_categorical_feature = ['lopsh', 'hocky', 'namhoc', 'ghichu']

# Điền dữ liệu thiếu bằng giá trị trung bình và làm tròn đến số nguyên
drl_df[drl_continuous_feature] = drl_df[drl_continuous_feature].fillna(drl_df[drl_continuous_feature].mean().round(0))

# Thay các giá trị > 100 thành 100 và < 0 thành 0 bằng
drl_df[drl_continuous_feature] = drl_df[drl_continuous_feature].applymap(lambda x: 100 if x > 100 else (0 if x < 0 else x))

# Thống kê mô tả cơ bản các cột dữ liệu liên tục
drl_df[drl_continuous_feature].describe().round(2)

# Trực quan hóa phân bố dữ liệu của các cột dữ liệu liên tục
plt.figure(figsize=(20,5))
plt.subplot(1,2,1)
sns.histplot(drl_df[drl_continuous_feature], kde=True, discrete=True)
plt.subplot(1,2,2)
sns.boxplot(drl_df[drl_continuous_feature])
plt.tight_layout()
plt.show()

# Chuyển các dữ liệu rời rạc về kiểu chuỗi
for col in drl_categorical_feature:
    drl_df[col] = drl_df[col].apply(lambda x: str(x))

# Xóa các ký tự đặc biệt của các dữ liệu rời rạc
for col in drl_categorical_feature:
    drl_df[col] = drl_df[col].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s\.]', '', x))

# Xác định các giá trị đặc trưng của dữ liệu rời rạc
# Đồng thời xác định các cột dữ liệu rời rạc đang chứa dữ liệu nhiễu
drl_df[drl_categorical_feature].apply(lambda x: len(x.unique()))

drl_df['nganhhoc'] = drl_df['lopsh'].apply(lambda x: re.sub(r'[^a-zA-Z]', '', x))

drl_df.head()

# Thay ' NULL' bằng ' ' để thống nhất việc nội dung ghi chú là rỗng
drl_df['ghichu'] = drl_df['ghichu'].replace(' NULL', ' ')

drl_df.head()

drl_df[drl_categorical_feature].describe()

drl_categorical_feature.extend(['nganhhoc'])
drl_categorical_plot_feature = drl_categorical_feature.copy()
drl_categorical_plot_feature.remove('lopsh')

print(drl_categorical_plot_feature)

# Trực quan hóa tần suất các giá trị đặc trưng dữ liệu rời rạc
col = 4
row = int(math.ceil(len(drl_categorical_plot_feature) / col))
plt.figure(figsize=(20,20))
plt.subplots_adjust(wspace=0.5, hspace=0.2)
for index, df_col in enumerate(drl_categorical_plot_feature):
    plt.subplot(row, col, index + 1)
    sns.countplot(drl_df[df_col])
plt.show()

# Chuyển đổi với xử lý lỗi và thay thế NaN bằng 0 (hoặc giá trị khác)
drl_df['hocky'] = pd.to_numeric(drl_df['hocky'], errors='coerce').fillna(0).astype(int)
drl_df['namhoc'] = pd.to_numeric(drl_df['namhoc'], errors='coerce').fillna(0).astype(int)

# Xuất dữ liệu sau khi xử lý
drl_df.to_excel("processed_10_diemrl.xlsx")

"""# ** 12.baoluu **"""

# Xác định các cột dữ liệu
bl_df.columns = bl_df.columns.str.strip() # xóa bỏ khoảng trắng thừa trong tên các cột
bl_cols = bl_df.columns.to_list()
bl_df.head()

# Xác định kiểu dữ liệu
bl_df.dtypes

# Tìm kiếm và xóa bỏ các dòng giá trị trống
print(bl_df.isnull().sum())
bl_df = bl_df.dropna(how='all')
print(bl_df.isnull().sum())

bl_cols

# Xác định các trường dữ liệu liên tục và rời rạc
bl_continuous_feature = []
bl_categorical_feature = ['tinhtrang', 'lydo', 'hocky', 'namhoc', 'soqd', 'ngayqd']

# Chuyển các dữ liệu rời rạc về kiểu chuỗi
for col in bl_categorical_feature:
    bl_df[col] = bl_df[col].apply(lambda x: str(x))

bl_df['lydo'].unique()

bl_df['lydo'] = bl_df['lydo'].replace(' TN', ' Tốt nghiệp')

bl_df['lydo'].unique()

bl_df.head()

bl_df['ngayqd'] = bl_df['ngayqd'].str.replace(r'\s*0+$', '', regex=True)

bl_df['ngayqd'] = bl_df['ngayqd'].str.replace(r'\s*0+$', '', regex=True)

bl_df.head()

# Xóa các ký tự hong hợp lệ của các dữ liệu rời rạc
for col in bl_categorical_feature:
    if col == 'lydo': continue
    bl_df[col] = bl_df[col].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s\./-]', '', x))

# Xác định các giá trị đặc trưng của dữ liệu rời rạc
# Đồng thời xác định các cột dữ liệu rời rạc đang chứa dữ liệu nhiễu
bl_df[bl_categorical_feature].apply(lambda x: len(x.unique()))

# Thống kê mô tả cơ bản dữ liệu rời rạc
bl_df[bl_categorical_feature].describe()

bl_categorical_plot_feature = bl_categorical_feature.copy()

# Trực quan hóa tần suất các giá trị đặc trưng dữ liệu rời rạc
col = 1
row = int(math.ceil(len(bl_categorical_plot_feature) / col))
plt.figure(figsize=(30,30))
plt.subplots_adjust(wspace=0.2, hspace=0.2)
for index, df_col in enumerate(bl_categorical_plot_feature):
    plt.subplot(row, col, index + 1)
    sns.countplot(bl_df[df_col])
plt.show()

bl_df['tinhtrang'] = pd.to_numeric(bl_df['tinhtrang'], errors='coerce').astype('Int64')
bl_df['hocky'] = pd.to_numeric(bl_df['hocky'], errors='coerce').astype('Int64')
bl_df['namhoc'] = pd.to_numeric(bl_df['namhoc'], errors='coerce').astype('Int64')

# Xuất dữ liệu sau khi xử lý
bl_df.to_excel("processed_12_baoluu.xlsx")

"""# ** 14.totnghiep **"""

# Xác định các cột dữ liệu
tn_df.columns = tn_df.columns.str.strip() # xóa bỏ khoảng trắng thừa trong tên các cột
tn_cols = tn_df.columns.to_list()
tn_df.head()

# Xác định kiểu dữ liệu
tn_df.dtypes

# Tìm kiếm và xóa bỏ các dòng giá trị trống
print(tn_df.isnull().sum())
tn_df = tn_df.dropna(how='all')
print(tn_df.isnull().sum())

tn_cols

# Xác định các trường dữ liệu liên tục và rời rạc
tn_continuous_feature = []
tn_categorical_feature = ['xeploai', 'soquyetdinh', 'ngaycapvb']

# Chuyển các dữ liệu rời rạc về kiểu chuỗi
for col in tn_categorical_feature:
    tn_df[col] = tn_df[col].apply(lambda x: str(x))

tn_df['xeploai'].unique()

tn_df['xeploai'] = tn_df['xeploai'].replace([' Trung bình Khá', ' TB Khá', ' TB khá'], ' Trung bình khá')

tn_df['xeploai'].unique()

# Xóa các ký tự hong hợp lệ của các dữ liệu rời rạc
for col in tn_categorical_feature[1:]:
    tn_df[col] = tn_df[col].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s\./-]', '', x))

# Xác định các giá trị đặc trưng của dữ liệu rời rạc
# Đồng thời xác định các cột dữ liệu rời rạc đang chứa dữ liệu nhiễu
tn_df[tn_categorical_feature].apply(lambda x: len(x.unique()))

# Thống kê mô tả cơ bản dữ liệu rời rạc
tn_df[tn_categorical_feature].describe()

tn_categorical_plot_feature = tn_categorical_feature.copy()

# Trực quan hóa tần suất các giá trị đặc trưng dữ liệu rời rạc
col = 3
row = int(math.ceil(len(tn_categorical_plot_feature) / col))
plt.figure(figsize=(30,15))
plt.subplots_adjust(wspace=0.2, hspace=0.2)
for index, df_col in enumerate(tn_categorical_plot_feature):
    plt.subplot(row, col, index + 1)
    sns.countplot(tn_df[df_col])
plt.show()

# Xuất dữ liệu sau khi xử lý
tn_df.to_excel("processed_14_totnghiep.xlsx")