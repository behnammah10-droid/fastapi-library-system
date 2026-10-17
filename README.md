# Books Library API

سیستم ساده مدیریت کتابخانه با استفاده از فریم‌ورک **FastAPI**.

## مسیرها (Endpoints)
- `GET /books` : دریافت لیست تمام کتاب‌ها
- `GET /books/{id}` : دریافت اطلاعات یک کتاب خاص
- `POST /books` : افزودن کتاب جدید
- `PATCH /books/{id}` : ویرایش اطلاعات کتاب
- `DELETE /books/{id}` : حذف کتاب

## نصب و اجرا
نصب کتابخانه‌ها:
```bash
pip install -r requirements.txt