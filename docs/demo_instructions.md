#   Hướng dẫn sử dụng Website Demo
## 1. Chuẩn bị môi trường
- Cài đặt Python (>= 3.8) và Node.js (>= 16).
- Cài đặt `pipenv`:
  ```bash
  pip install pipenv
  ```

## 2. Tạo cấu trúc thư mục
Tạo các thư mục chính cho dự án:
```bash
mkdir backend frontend
```

## 3. Thiết lập Backend Django
```bash
pipenv shell
pipenv install -r requirements.txt
```

## 4. Thiết lập Frontend ReactJS
```bash
cd frontend
npm install
```

## 5. Chạy dự án
### a. Chạy Backend Server
```bash
pipenv shell
cd backend
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### b. Chạy Frontend Server
```bash
cd frontend
npm start
```

## 7. Kiểm tra và hoàn thiện
- Mở trình duyệt tại `http://localhost:3000` để kiểm tra giao diện frontend.
- Backend API sẽ hoạt động tại `http://localhost:8000`.
