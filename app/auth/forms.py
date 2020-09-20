from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required, Email, EqualTo

class SignUpform(FlaskForm):
    username = StringField('Preferd username ', validators=[Required()])
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required(),EqualTo('confirm_password', message='Your passwords do not match')])
    confirm_password = PasswordField('Confirm Password', validators=[Required()])

class SignInForm(FlaskForm):
    username = StringField('Username ', validators=[Required()])
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])