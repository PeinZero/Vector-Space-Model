from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField


class Searching(FlaskForm):
    searched = StringField()
    alpha = DecimalField()
    submit = SubmitField()