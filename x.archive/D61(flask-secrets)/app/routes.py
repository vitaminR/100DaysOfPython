from flask import Blueprint, render_template, request, redirect, url_for, flash

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/access_denied")
def access_denied():
    return render_template("denied.html")


@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Example logic: simple check (replace with actual authentication logic)
        if username == "admin" and password == "password":
            return redirect(url_for("main.success"))
        else:
            flash("Invalid credentials. Please try again.", "danger")
            return redirect(url_for("main.login"))
    return render_template("login.html")


@main.route("/success")
def success():
    return render_template("success.html")
