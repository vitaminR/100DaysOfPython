from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap4

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "your_secret_key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
    Bootstrap4(app)
    db.init_app(app)

    from .routes import main
    from .models import Cafe  # Import the Cafe model

    app.register_blueprint(main)

    with app.app_context():
        db.create_all()  # Create the database and tables

    return app
