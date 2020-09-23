import unittest
from app import db
from app.models import Pitch,User,Review

class TestReview(unittest.TestCase):

    def setUp(self):
        self.new_user = User(user_id = 4000,user_name = 'Sandy', user_email = 'sandys@gmail', user_password = 'Stanford1*')
        self.new_pitch = Pitch(pitch_id = 2000, category = 'Pick uplines', Pitch = 'Car engine', user = self.new_user,)

    def tearDown(self):
        Pitch.query.delete()
    

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch_id,2000)
        self.assertEquals(self.new_pitch.category,'Pick uplines')
        self.assertEquals(self.new_pitch.Pitch,'Car engine')
        self.assertEquals(self.new_pitch.user,self.new_user)

    def test_review_saving(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all()) >0)
      