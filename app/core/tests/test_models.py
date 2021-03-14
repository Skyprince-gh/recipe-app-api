from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

  def test_create_user_with_emamil_successful(self):
    """Test creating a new user with an email is successful"""
    email = 'test@test.com'
    password = 'testpass123'

    user = get_user_model().objects.create_user( #call the create user function from the user model do not import models directly
      email=email, #adds email note all these are custom properties since the user model will be changed
      password=password #add password note all these are custom properties since the user model will be changed
      )

    self.assertEqual(user.email, email)
    self.assertTrue(user.check_password, password) #you use the check_password function because passwords are encrypted