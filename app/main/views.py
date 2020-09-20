from flask import render_template, redirect, url_for
from ..models import User, Pitch
from . import main
from .. import db
from .forms import NewPitchForm
from ..models import Pitch

@main.route('/')
def pitch():

    pitches = Pitch.query.all()
    title = 'Pitches'

    return render_template('index.html', pitches = pitches, title = title)

@main.route('/reviews/<int:id>')
def review(id):

    title = 'Reviews'

    return render_template('reviews.html', title = title)

@main.route('/add_Pitch')
def newpitch():

    form = NewPitchForm()

    if form.validate_on_submit():
        category = form.category.data
        Pitch = form.pitch.data

        newpitch = Pitch(category,Pitch)

    title = 'New pitch'

    return render_template('newpitch.html', title = title)