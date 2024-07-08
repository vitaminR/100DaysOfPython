from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class MovieForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    director = StringField("Director", validators=[DataRequired()])
    year = StringField("Year", validators=[DataRequired()])
    rating = FloatField(
        "Rating", validators=[DataRequired(), NumberRange(min=0, max=10)]
    )
    submit = SubmitField("Submit")


class RateMovieForm(FlaskForm):
    rating = FloatField(
        "Rating", validators=[DataRequired(), NumberRange(min=0, max=10)]
    )
    review = StringField("Review", validators=[DataRequired()])
    submit = SubmitField("Submit")
