import wtforms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddTaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = wtforms.TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Submit')
