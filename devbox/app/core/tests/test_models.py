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
    self.assertTrue(user.check_password(password)) #you use the check_password function because passwords are encrypted

  def test_new_user_email_normalized(self):
    """Test the email for a new user is normalized"""

    email = 'test@TEST.com'
    user = get_user_model().objects.create_user(email, 'adsfhkjhd' );

    self.assertEqual(user.email, email.lower()) #test if email is equal to lowercase version of the email.

  

  def test_new_user_invalid_email(self):
    """Test creating user with no email raises error """
    with self.assertRaises(ValueError):
      get_user_model().objects.create_user(None, 'test123')

  
  def test_create_new_superuser(self):
    """Testing create new superuser"""

    user = get_user_model().objects.create_superuser(
      'test@test.com',
      'test1234'
    )

    #assert true is used for boolean operations. 
    self.assertTrue(user.is_superuser) #get the boolean value
    self.assertTrue(user.is_staff) #get the boolean value.