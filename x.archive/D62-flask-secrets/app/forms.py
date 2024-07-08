from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL


class CafeForm(FlaskForm):
    name = StringField("Cafe Name", validators=[DataRequired()])
    location = StringField(
        "Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()]
    )
    open = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    close = StringField("Closing Time e.g. 5PM", validators=[DataRequired()])
    coffee = StringField("Coffee Rating", validators=[DataRequired()])
    wifi = StringField("Wifi Strength Rating", validators=[DataRequired()])
    power = StringField("Power Socket Availability", validators=[DataRequired()])
    submit = SubmitField("Submit")
