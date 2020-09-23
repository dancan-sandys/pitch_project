import  unittest
from app.models import User
from app import db

class TestUser(unittest.TestCase):

    def setUp(self):
        self.new_user = User(user_id = 200,user_name = 'Sandy', user_email = 'sandys@gmail', user_password = 'Stanford1*')


    def tearDown(self):
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_user, User))

    
    def test_check_instance_variables(self):
        self.assertEquals(self.new_user.user_id,200)
        self.assertEquals(self.new_user.user_name,'Sandy')
        self.assertEquals(self.new_user.user_email,"sandys@gmail")
        self.assertEquals(self.new_user.user_password,'Stanford1*')
       
