from . import db
from datetime import datetime

class Pitch(db.Model):

    __tablename__ = 'pitches'

    pitch_id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.String)
    Pitch = db.Column(db.String)
    Posting = db.Column(db.DateTime, default = datetime.utcnow)



    

class Review(db.Model):
    __tablename__ = 'reviews'

    review_id = db.Column(db.Integer, primary_key = True)
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)
    comment = db.Column(db.String)


class User(db.model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(255))
    user_email = db.Column(db.String(255))
    user_password = db.Column(db.String(255))

