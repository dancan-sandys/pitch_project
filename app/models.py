from . import db
from flask_login import UserMixin
from datetime import datetime
from. import login_manager

class Pitch(db.Model):

    __tablename__ = 'pitches'

    pitch_id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.String)
    Pitch = db.Column(db.String)
    Posting = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    reviews = db.relationship('Review', backref = 'pitch', lazy = 'dynamic')

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()


    

class Review(db.Model):
    __tablename__ = 'reviews'

    review_id = db.Column(db.Integer, primary_key = True)
    # upvotes = db.Column(db.Integer)
    # downvotes = db.Column(db.Integer)
    comment = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.pitch_id"))


    def save_review(self):
        
        db.session.add(self)
        db.session.commit()


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(255))
    user_email = db.Column(db.String(255))
    user_password = db.Column(db.String(255))
    profile_pic = db.Column(db.String)
    User_bio = db.Column(db.String)
    pitches = db.relationship('Pitch', backref = 'user', lazy = 'dynamic')
    reviews = db.relationship('Review', backref = 'user', lazy = 'dynamic')
    



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))