from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin 
# Create your models here.

# This will help use create a user providing the email and the password
class UserManager(BaseUserManager):
  """Custom user creation class"""

  def create_user(self,email,password=None, **extra_fields):
    """Creates and saves a new user"""

    if not email: 
      raise ValueError('Users must have an email address')
    #sets the email field of your user model, this is done on the model itself because there are no functions to change it.
    user = self.model(email=self.normalize_email(email), **extra_fields) 
    user.set_password(password)
    user.save(using=self._db) #save using the defualt database in the settings.py file.

    return user

  def create_superuser(self, email, password):
    """Creates and saves a new super user"""
    user = self.create_user(email, password)
    user.is_staff = True
    user.is_superuser = True
    user.save(using=self._db)

    return user

#we will override this user model class to ressetting the defualt behaviour of the user model
class User (AbstractBaseUser, PermissionsMixin):
  """"Custom user model that supports using email instead of username"""

  email = models.EmailField(max_length=255, unique=True) #you can only create one user with that email
  name = models.CharField(max_length=255)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)

  objects = UserManager()

  USERNAME_FIELD = 'email' #we are setting the username field to email so it accepts email in the username instead.
