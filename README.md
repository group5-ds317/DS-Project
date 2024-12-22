# DS-Project - Hệ thống khuyến nghị môn học cho sinh viên UIT từ dữ liệu học tập

## Mô tả dự án
Dự án này phát triển một hệ thống khuyến nghị môn học dựa trên dữ liệu học tập cá nhân của sinh viên. Mục tiêu là hỗ trợ sinh viên tối ưu hóa lộ trình học tập, cải thiện điểm số, giảm nguy cơ rớt môn và nâng cao trải nghiệm học tập. 

## Mục tiêu chính
1. **Phân tích dữ liệu học tập**: Xử lý và tích hợp dữ liệu lịch sử học tập của sinh viên.
2. **Xây dựng hệ thống khuyến nghị**: Ứng dụng các thuật toán học máy để gợi ý môn học phù hợp với năng lực và mục tiêu cá nhân.
3. **Phát triển nền tảng website**: Cung cấp giao diện thân thiện, hỗ trợ sinh viên đăng ký môn học một cách dễ dàng.

## Phạm vi ứng dụng
- **Ngữ cảnh**: Hỗ trợ sinh viên tại Trường Đại học Công nghệ Thông tin (UIT) trong việc chọn môn học phù hợp.
- **Dữ liệu**: Tập trung vào kết quả học tập, thông tin môn học và chương trình đào tạo của UIT.
- **Hạn chế**: Hệ thống hiện chỉ thử nghiệm trên dữ liệu UIT, chưa mở rộng ra các trường khác.

## Công nghệ sử dụng
- **Backend**: Django
- **Frontend**: React
- **Thuật toán**: Ma trận tương đồng Cosine, K-Means, Mô hình học sâu (MLP), và PhoBERT.

## Các tính năng chính
1. **Khuyến nghị môn học cá nhân hóa**:
   - Dựa trên lịch sử học tập, kết quả điểm số và sở thích cá nhân.
   - Gợi ý các môn học giúp tối ưu hóa kết quả học tập.
2. **Hỗ trợ lập kế hoạch học tập**:
   - Đề xuất lộ trình học tập dài hạn phù hợp.
   - Gợi ý cách cải thiện điểm số và đạt các mục tiêu học thuật.
3. **Giao diện trực quan**:
   - Thiết kế thân thiện, dễ sử dụng, tích hợp tính năng đăng ký môn học.

## Hướng phát triển
- Mở rộng áp dụng cho các trường đại học khác.
- Tích hợp thêm dữ liệu từ giảng viên, phản hồi sinh viên, và yêu cầu thị trường lao động.
- Nâng cấp mô hình khuyến nghị với các thuật toán tiên tiến hơn như GNN hoặc GPT.
- Tăng cường bảo mật và bảo vệ dữ liệu cá nhân sinh viên.

## Đóng góp
Dự án được thực hiện bởi nhóm sinh viên lớp DS317.P11 dưới sự hướng dẫn của ThS. Nguyễn Thị Anh Thư:
- Phan Thanh Hải (MSSV: 22520390)
- Trương Hồng Anh (MSSV: 22520084)
- Trương Huỳnh Thúy An (MSSV: 22520033)
- Nguyễn Hải Đăng (MSSV: 22520189)
- Lê Trần Gia Bảo (MSSV: 22520105)

## Liên hệ
Mọi ý kiến đóng góp hoặc câu hỏi, vui lòng liên hệ nhóm qua email: [22520390@gm.uit.edu.vn](mailto:22520390@gm.uit.edu.vn).

##   Hướng dẫn sử dụng Website Demo
### 1. Chuẩn bị môi trường
- Cài đặt Python (>= 3.8) và Node.js (>= 16).
- Cài đặt `pipenv`:
  ```bash
  pip install pipenv
  ```

### 2. Tạo cấu trúc thư mục
Tạo các thư mục chính cho dự án:
```bash
mkdir backend frontend
```

### 3. Thiết lập Backend Django
```bash
pipenv shell
pipenv install -r requirements.txt
```

### 4. Thiết lập Frontend ReactJS
```bash
cd frontend
npm install
```

### 5. Chạy dự án
#### a. Chạy Backend Server
```bash
pipenv shell
cd backend
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

#### b. Chạy Frontend Server
```bash
cd frontend
npm start
```

### 7. Kiểm tra và hoàn thiện
- Mở trình duyệt tại `http://localhost:3000` để kiểm tra giao diện frontend.
- Backend API sẽ hoạt động tại `http://localhost:8000`.
