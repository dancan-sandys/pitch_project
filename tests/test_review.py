import unittest
from app import db
from app.models import Review,User

class TestReview(unittest.TestCase):

    def setUp(self):
        self.new_user = User(user_id = 3000,user_name = 'Sandy', user_email = 'sandys@gmail', user_password = 'Stanford1*')
        self.new_review = Review(review_id = 12300, comment = 'Yes Yes', user = self.new_user)
    
    def tearDown(self):
        Review.query.delete()
        User.query.delete()   


    def test_instance(self):
        self.assertTrue(isinstance(self.new_review,Review))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_review.review_id,12300)
        self.assertEquals(self.new_review.comment,'Yes Yes')
        self.assertEquals(self.new_review.user,self.new_user)

    def test_review_saving(self):
        self.new_review.save_review()
        self.assertTrue(len(Review.query.all()) >0)
      