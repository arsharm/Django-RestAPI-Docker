from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,\
                                        PermissionsMixin

# Create your models here.


class UserManager(BaseUserManager):
    """User Manager Class
    """

    def create_user(self, email, password, **extra_fields):
        """Create a new user

        Args:
            email (string): user email address
            password (string): user password
        """

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email),  **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_super_user(self, email, password):

        """Create new super user"""

        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports email instead of username
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
