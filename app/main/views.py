from flask import render_template, redirect, url_for
from ..models import User, Pitch,Review
from . import main
from .. import db
from .forms import NewPitchForm, ReviewForm
from ..models import Pitch

@main.route('/')
def pitch():

    pitches = Pitch.query.all()
    title = 'Pitches'

    return render_template('index.html', pitches = pitches, title = title)

@main.route('/reviews/<int:id>', methods = ['GET', 'POST'])
def review(id):

    title = 'Reviews'

    pitch = Pitch.query.filter_by(pitch_id = id).first()
    form = ReviewForm()
    if form.validate_on_submit():
        
        form = ReviewForm()

        comment = form.comment.data
        pitch_id = id

        new_review = Review(comment = comment, pitch_id = pitch_id)

        pitch_reviews = pitch.query.filter_by(pitch_id = pitch_id).all()

        return render_template('reviews.html', title = title, pitch = pitch, form =form)


    return render_template('reviews.html', title = title, pitch = pitch, form = form)

@main.route('/add_Pitch', methods = ['GET','POST'])
def newpitch():

    form = NewPitchForm()

    if form.validate_on_submit():
        category = form.category.data
        Pitch_body = form.pitch.data

        new_pitch = Pitch(category = category,Pitch = Pitch_body)

        new_pitch.save_pitch()

        return redirect(url_for('.pitch'))

    
    title = 'New pitch'

    return render_template('newpitch.html', title = title, form = form)