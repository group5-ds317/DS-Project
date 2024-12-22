# Kiến Trúc Hệ Thống Khuyến Nghị Môn Học Dựa Trên Lịch Sử Học Tập Của Sinh Viên UIT

## 1. Tổng Quan

Hệ thống khuyến nghị môn học được xây dựng nhằm cung cấp cho sinh viên UIT những gợi ý về môn học dựa trên lịch sử học tập của họ. Hệ thống này không chỉ giúp sinh viên lựa chọn môn học phù hợp mà còn hỗ trợ họ trong việc tối ưu hóa lịch học và cải thiện kết quả học tập. Hệ thống bao gồm các bước tiền xử lý dữ liệu, xử lý dữ liệu, mô hình hóa và đánh giá.

---

## 2. Các Bước Tiền Xử Lý Dữ Liệu

### 2.1. Tiền Xử Lý Dữ Liệu Sinh Viên và Điểm

#### 2.1.1. Đọc Dữ Liệu

Sử dụng thư viện `pandas` để đọc dữ liệu từ các file Excel chứa thông tin sinh viên và điểm. Việc này giúp dễ dàng quản lý và thao tác với dữ liệu.

```python
import pandas as pd

sv_df = pd.read_excel("path_to_students_data.xlsx")
diem_df = pd.read_excel("path_to_scores_data.xlsx")
```

#### 2.1.2. Xử Lý Dữ Liệu Trống

- **Loại Bỏ Dữ Liệu Trống**: Sử dụng phương pháp `dropna` để loại bỏ các dòng không có giá trị.
- **Điền Dữ Liệu Thiếu**: Đối với các trường dữ liệu liên tục, điền giá trị thiếu bằng giá trị trung bình của cột.

```python
sv_df = sv_df.dropna(how='all')
sv_df.fillna(sv_df.mean(), inplace=True)
```

#### 2.1.3. Chuẩn Hóa Dữ Liệu

- **Chuyển Đổi Kiểu Dữ Liệu**: Chuyển đổi các trường dữ liệu rời rạc thành kiểu chuỗi để dễ dàng xử lý.
- **Loại Bỏ Ký Tự Đặc Biệt**: Sử dụng biểu thức chính quy để loại bỏ các ký tự không mong muốn trong dữ liệu.

```python
import re

pattern = r'[!\"#\$%&\'\(\)\*\+,\-\./:;<=>\?@\[\\\]\^_`\{\|\}~]'
sv_df['column_name'] = sv_df['column_name'].apply(lambda x: re.sub(pattern, '', x))
```

### 2.2. Tiền Xử Lý Dữ Liệu Khác

#### 2.2.1. Xử Lý Dữ Liệu Tốt Nghiệp và Bảo Lưu

Thực hiện các bước xử lý tương tự cho dữ liệu tốt nghiệp và bảo lưu, nhằm đảm bảo tính toàn vẹn và đồng nhất của dữ liệu.

---

## 3. Xử Lý Dữ Liệu

### 3.1. Nối Dữ Liệu

- **Kết Nối Các Bảng Dữ Liệu**: Sử dụng phương pháp `pd.merge` để kết nối dữ liệu từ các bảng khác nhau dựa trên mã sinh viên (`mssv`).

```python
merged_df = pd.merge(sv_df, diem_df, on='mssv', how='inner')
```

### 3.2. Lọc và Gộp Dữ Liệu

- **Lọc Dữ Liệu**: Chọn các thuộc tính cần thiết cho hệ thống khuyến nghị như mã sinh viên, giới tính, khoa, và điểm.
- **Gộp Dữ Liệu**: Gộp dữ liệu từ kỳ 3 vào kỳ 2 để có thông tin đầy đủ hơn về kết quả học tập.

### 3.3. Tạo Dữ Liệu Mở Rộng

- **Mở Rộng Dữ Liệu**: Kết nối với các bảng mô tả môn học để lấy thêm thông tin về môn học, giúp cải thiện độ chính xác của mô hình khuyến nghị.

### 3.4. Word Embedding

- **Sử Dụng PhoBERT**: Tạo embeddings cho các mô tả môn học bằng cách sử dụng mô hình PhoBERT, giúp hệ thống hiểu rõ hơn về nội dung môn học.

---

## 4. Mô Hình

### 4.1. Mô Hình Khuyến Nghị

#### 4.1.1. Lớp Mô Hình

Tạo lớp `Model` để định nghĩa các phương thức khuyến nghị, bao gồm:

- **Khuyến Nghị Môn Học**: Dựa trên độ phổ biến và lịch sử học tập của sinh viên, mô hình sẽ gợi ý những môn học phù hợp.
- **Đánh Giá Môn Học**: Tính toán độ chính xác, độ nhạy và điểm F1 cho các môn học được khuyến nghị.

```python
class Model:
    def __init__(self, student_df, score_df):
        self.student_df = student_df
        self.score_df = score_df

    def recommend_courses(self):
        # Logic to recommend courses
        pass
```

---

## 5. Đánh Giá

### 5.1. Đánh Giá Mô Hình

- **Chỉ Số Đánh Giá**: Sử dụng các chỉ số như độ chính xác, độ nhạy và điểm F1 để đánh giá hiệu suất của mô hình khuyến nghị. Các chỉ số này giúp xác định mức độ chính xác và khả năng dự đoán của mô hình.

```python
from sklearn.metrics import accuracy_score, f1_score

# Giả định có y_true và y_pred
accuracy = accuracy_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred, average='weighted')
```

---

## 6. Kiến Trúc Website Ứng Dụng

### 6.1. Kiến Trúc Client-Server

- **Client**: 
  - **ReactJS**: Giao diện người dùng được xây dựng bằng ReactJS, cho phép sinh viên tương tác với hệ thống khuyến nghị một cách trực quan và dễ dàng.

- **Server**: 
  - **Django**: Xử lý các yêu cầu từ client và thực hiện các thao tác với cơ sở dữ liệu, đảm bảo an toàn và hiệu quả trong việc quản lý dữ liệu.

- **Database**: 
  - **PostgreSQL**: Lưu trữ dữ liệu sinh viên, điểm, và thông tin môn học, đảm bảo tính toàn vẹn và bảo mật của dữ liệu.

### 6.2. Giao Tiếp Qua API

- **RESTful API**: Giao tiếp giữa client và server được thực hiện thông qua các API RESTful, cho phép gửi và nhận dữ liệu một cách hiệu quả và linh hoạt.

---

## 7. Sơ Đồ Kiến Trúc

````artifact
id: architecture_diagram
name: Kiến Trúc Hệ Thống Khuyến Nghị Môn Học
type: mermaid
content: |-
  graph TD;
      A[Client: ReactJS] -->|Gửi yêu cầu| B[Server: Django];
      B -->|Truy vấn| C[Database: PostgreSQL];
      C -->|Trả dữ liệu| B;
      B -->|Gửi phản hồi| A;
      B -->|Chạy mô hình khuyến nghị| D[Model];
      D -->|Truy cập dữ liệu| C;
