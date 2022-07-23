from django.db.models import *
from django.db import transaction
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils import timezone


# methods for save users
class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise
 
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
 
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
 
        return self._create_user(email, password=password, **extra_fields)

# table for saved users
class User(AbstractBaseUser,PermissionsMixin):
    email=EmailField(max_length=150,unique=True)
    first_name=CharField(max_length=200,blank=True)
    last_name=CharField(max_length=200,blank=True)
    is_active=BooleanField(default=True)
    is_staff=BooleanField(default=False)
    data_joined=DateTimeField(default=timezone.now)
    
    objects=UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
 
    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self
