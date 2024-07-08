from flask import Blueprint, render_template, redirect, url_for, request
from app import db
from app.models import Cafe

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/cafes")
def cafes():
    cafes = Cafe.query.all()
    return render_template("cafes.html", cafes=cafes)


@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Process login form
        pass
    return render_template("login.html")
