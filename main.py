from fastapi import FastAPI

app = FastAPI()

# لیست کتاب‌ها (دیتابیس فرضی داخل متغیر)
books = [
    {"id": 1, "title": "Python Programming", "author": "Guido van Rossum"},
    {"id": 2, "title": "C++ Primer", "author": "Stanley B. Lippman"},
    {"id": 3, "title": "Effective Java", "author": "Joshua Bloch"}
]


# دریافت لیست کتاب‌ها
@app.get("/books")
async def get_all_books():
    return books


# دریافت اطلاعات یک کتاب خاص
@app.get("/books/{id}")
async def get_book_by_id(id: int):
    for book in books:
        if book["id"] == id:
            return book
    return {"message": "Book not found (404)"}


# اضافه کردن کتاب جدید
@app.post("/books")
async def add_new_book(title: str, author: str):
    # پیدا کردن آخرین آیدی و اضافه کردن ۱ واحد به آن (بدون باگ)
    if len(books) > 0:
        new_id = books[-1]["id"] + 1
    else:
        new_id = 1
        
    new_book = {
        "id": new_id,
        "title": title,
        "author": author
    }
    books.append(new_book)
    return {"message": "New book added successfully", "book": new_book}


# تغییر اطلاعات یک کتاب خاص
@app.patch("/books/{id}")
async def update_book(id: int, title: str = None, author: str = None):
    for book in books:
        if book["id"] == id:
            if title is not None:
                book["title"] = title
            if author is not None:
                book["author"] = author
            return {"message": "Book information updated", "book": book}
            
    return {"message": "Book not found (404)"}


# حذف یک کتاب خاص
@app.delete("/books/{id}")
async def delete_book(id: int):
    for book in books:
        if book["id"] == id:
            books.remove(book)
            return {"message": "Book successfully deleted"}
            
    return {"message": "Book not found (404)"}