def upvote(pitch_id):
    
    Pitch.query.filter_by(pitch_id = pitch_id).first().update({"votes": "votes + 1"})
def downvote(pitch_id):

    Pitch.query.filter_by(pitch_id = pitch_id).first().update({"votes": "votes + 1"})