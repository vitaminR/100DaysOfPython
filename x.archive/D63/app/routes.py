from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Book

main = Blueprint("main", __name__)


@main.route("/")
def index():
    books = Book.query.all()
    return render_template("index.html", books=books)


@main.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"],
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("main.index"))
    return render_template("add.html")


@main.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    book = Book.query.get_or_404(id)
    if request.method == "POST":
        book.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("main.index"))
    return render_template("edit_rating.html", book=book)


@main.route("/delete/<int:id>")
def delete(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("main.index"))
