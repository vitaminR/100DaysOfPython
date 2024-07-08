# D63/populate_db.py
from app import create_app, db
from app.models import Book

app = create_app()

with app.app_context():
    db.create_all()

    book1 = Book(title="Book 1", author="Author 1", genre="Genre 1")
    book2 = Book(title="Book 2", author="Author 2", genre="Genre 2")

    db.session.add(book1)
    db.session.add(book2)
    db.session.commit()
