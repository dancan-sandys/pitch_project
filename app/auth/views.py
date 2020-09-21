from flask import render_template, render_template,request, url_for
from . import auth
from .forms import SignUpform, SignInForm
from flask_login import login_user


@auth.route('/signup', methods= ["GET","POST"])
def signup():

    form = SignUpform

    if form.validate_on_submit():

        user = User(user_email =form.email.data, user_username = form.username.data, user_password = form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.signin'))

        title = 'New Account'

    return render_template('signup.html')


@auth.route('/signin')
def signin():
    form = SignInForm

    if form.validate_on_submit():

        user = User.query.filter_by(email = form.email.data).first()

        if user is not None:
            login_user(user, login_form,remember.data)
