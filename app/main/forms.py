from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField, SelectField
from wtforms.validators import Required


class ReviewForm(FlaskForm):

    comment = TextAreaField('Enter your comments', validators=[Required()])
    submit = SubmitField('Submit')

class NewPitchForm(FlaskForm):

    category = SelectField('Category', validators=[Required()], choices=['Pickup lines', 'interview pitch', 'product pitch', 'promotion pitch'])
    pitch = TextAreaField('Pitch', validators=[Required()])
    submit = SubmitField('Submit')

class ProfileForm(FlaskForm):

    bio = StringField('Say something about yourself')