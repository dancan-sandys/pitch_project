from flask import render_template,flash,redirect, render_template,request, url_for
from . import auth
from .forms import SignUpform, SignInForm
from flask_login import login_user
from ..models import User
from .. import db

@auth.route('/signup', methods= ["GET","POST"])
def signup():

    form = SignUpform()

    if form.validate_on_submit():

        user = User(user_email =form.email.data, user_name = form.username.data, user_password = form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.login'))

        title = 'New Account'

    return render_template('auth/signup.html', form = form)


@auth.route('/signin', methods = ["GET","POST"])
def login():
    form = SignInForm()

    if form.validate_on_submit():

        user = User.query.filter_by(user_email = form.email.data).first()

        if user is not None:
            login_user(user, login_form.remember.data)
            return redirect(request.args.get('next') or url_for('index.html'))

        flash ('invalid username or password')

    title = 'Loging in'
    return render_template('auth/login.html', form = form, title  = title)