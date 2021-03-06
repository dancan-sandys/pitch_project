from flask import render_template, redirect, url_for, request
from ..models import User, Pitch,Review
from . import main
from .. import db, photos
from .forms import NewPitchForm, ReviewForm, ProfileForm
from ..models import Pitch
from flask_login import login_required, current_user


@main.route('/')
def pitch():

    pitches = Pitch.query.all()
    title = 'Pitches'

    return render_template('index.html', pitches = pitches, title = title)

@main.route('/categories')
def categories():

    pitches = Pitch.query.all()
    title = 'Pitches'

    return render_template('categorised.html', pitches = pitches, title = title)

@main.route('/reviews/<int:id>', methods = ['GET', 'POST'])
@login_required
def review(id):

    title = 'Reviews'

    pitch = Pitch.query.filter_by(pitch_id = id).first()
    form = ReviewForm()
    if form.validate_on_submit():
        
        form = ReviewForm()

        comment = form.comment.data
        pitch_id = id

        new_review = Review(comment = comment, pitch_id = pitch_id)

        new_review.save_review()

        pitch_reviews = Review.query.filter_by(pitch_id = pitch_id).all()

        return render_template('reviews.html', title = title, pitch = pitch, form =form, pitch_reviews = pitch_reviews)


    return render_template('reviews.html', title = title, pitch = pitch, form = form)

@main.route('/add_Pitch', methods = ['GET','POST'])
@login_required
def newpitch():

    form = NewPitchForm()

    if form.validate_on_submit():
        category = form.category.data
        Pitch_body = form.pitch.data

        new_pitch = Pitch(category = category,Pitch = Pitch_body, votes = 0)

        new_pitch.save_pitch()

        return redirect(url_for('.pitch'))

    
    title = 'New pitch'

    return render_template('newpitch.html', title = title, form = form)

@main.route('/profile/<uname>')
@login_required
def profile(uname):

    user = User.query.filter_by(user_name = uname).first()
    user_id =user.user_id
    pitches = Pitch.query.filter_by(user_id = user_id).all()



    if user is None:

        abort(404)

    return render_template("profile/profile.html", user = user, pitches = pitches)


@main.route('/profile/form/<uname>', methods= ['POST','GET'])
def profileupdate(uname):

    user = User.query.filter_by(user_name = uname).first()

    if user is None:

        abort(404)




    form = ProfileForm()

    if form.validate_on_submit():
        user.User_bio= form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname =user.user_name))

    return render_template('profile/updateprofile.html',form =form)

@main.route('/user/<uname>/update/pic', methods =['POST'])
def update_pic(uname):

    user =User.query.filter_by(user_name = uname).first()

    if 'photo' in request.files:

        filename = photos.save(request.files['photo'])
        path  = f'photos/{filename}'
        user.profile_pic = path
        db.session.commit()

    return redirect(url_for('.profile', uname = user.user_name))