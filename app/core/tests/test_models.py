from django.test import TestCase
from django.contrib.auth import get_user_model


#####           Notes

##          get_user_model calls the default user functions which are overriden of sorts in User model class and User Manager classes
##          
##
##
##
##

class ModelTests(TestCase):

    def test_create_user_email_successful(self):
        """Test creating a new user with email is successful
        """
        email="testemail@airbase.io"
        password="Test@123"
        user=get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(email,user.email)
        self.assertTrue(user.check_password(password))


    def test_create_new_user_email_successful(self):
        """Test creating a new user with same email is successful
        """
        email="testemail@Airbase.io"
        password="Test@123"
        user=get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(email.lower(),user.email)
    
    def test_create_user_invalid_email(self):
        """Test if Value Error is raised is user email is not provided
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'pwd123')
    
    def test_create_super_user(self):
        """Test creating a new super user"""

        email="testemail@Airbase.io"
        password="Test@123"
        user=get_user_model().objects.create_super_user(
            email=email,
            password=password
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
      