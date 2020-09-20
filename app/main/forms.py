from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField, 
from wtforms.validators import Required, 


class ReviewForm(FlaskForm):

    comment = TextAreaField('Enter your comments', validators=[Required])
    submit = SubmitField('Submit')

