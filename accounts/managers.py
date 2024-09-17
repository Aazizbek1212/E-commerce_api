from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password



class UserManager(BaseUserManager):
    """ create and save a new user"""
    def create_user(self, phone_number, password=None, **extra_fields):

        if not phone_number:
            raise ValueError('Users must have an phone_number address')
        user = self.model(phone_number=phone_number, **extra_fields, password=make_password(password))
        user.save(using=self._db)

        return user
   
    """ create and save a new superuser"""
    def create_superuser(self, phone_number, password):
        user = self.create_user(phone_number, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
    