from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Required, Email, EqualTo
from ..models import User
from wtforms import ValidationError

class SignUpform(FlaskForm):
    username = StringField('Preferd username ', validators=[Required()])
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required(),EqualTo('confirm_password', message='Your passwords do not match')])
    confirm_password = PasswordField('Confirm Password', validators=[Required()])
    submit = SubmitField('Sign Up')


    def validate_email(self,data_field):
        if User.query.filter_by(user_email =data_field.data).first():
            raise ValidationError('There is an account with that email address')

    def validate_username(self,data_field):
        if User.query.filter_by(user_name = data_field.data).first():
            raise ValidationError('The username is already taken')





class SignInForm(FlaskForm):
    username = StringField('Username ', validators=[Required()])
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember  =BooleanField('Remember me')
    submit = SubmitField('Sign in')

