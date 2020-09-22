from flask import render_template,flash,redirect, render_template,request, url_for
from . import auth
from .forms import SignUpform, SignInForm
from flask_login import login_user, logout_user, login_required
from .. import db
from ..email import mail_message

from ..models import User
@auth.route('/signup', methods= ["GET","POST"])
def signup():

    form = SignUpform()

    if form.validate_on_submit():

        user = User(user_email =form.email.data, user_name = form.username.data, user_password = form.password.data)
        db.session.add(user)
        db.session.commit()

        mail_message("Welcome to the Pitch", "email/Welcome user", user.user_email, user =user)
        return redirect(url_for('.login'))

        title = 'New Account'

    return render_template('auth/signup.html', form = form)


@auth.route('/signin', methods = ["GET","POST"])
def login():
    form = SignInForm()

    if form.validate_on_submit():

        user = User.query.filter_by(user_email = form.email.data).first()

        if user is not None:
            login_user(user, form.remember.data)
            return redirect(request.args.get('next') or url_for('index.html'))

        flash ('invalid username or password')

    title = 'Loging in'
    return render_template('auth/login.html', form = form, title  = title)

@auth.route('/logout', methods = ['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.pitch"))