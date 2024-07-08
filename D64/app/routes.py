from flask import Blueprint, render_template, redirect, url_for, flash, request
from .models import Movie
from .forms import MovieForm, RateMovieForm
from . import db

main = Blueprint("main", __name__)


@main.route("/")
def index():
    movies = Movie.query.all()
    return render_template("index.html", movies=movies)


@main.route("/add", methods=["GET", "POST"])
def add_movie():
    form = MovieForm()
    if form.validate_on_submit():
        new_movie = Movie(
            title=form.title.data,
            director=form.director.data,
            year=form.year.data,
            rating=form.rating.data,
        )
        db.session.add(new_movie)
        db.session.commit()
        flash("Movie added successfully!", "success")
        return redirect(url_for("main.index"))
    return render_template("add_movie.html", form=form)


@main.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_movie(id):
    movie = Movie.query.get_or_404(id)
    form = RateMovieForm()
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        flash("Movie updated successfully!", "success")
        return redirect(url_for("main.index"))
    elif request.method == "GET":
        form.rating.data = movie.rating
        form.review.data = movie.review
    return render_template("edit_movie.html", form=form, movie=movie)
