################################   Authntication  ###########################################                                         

# Login in JWT

- setup 
    pip install djangorestframework-simplejwt

    in INSTALLED_APPS=[
         'rest_framework_simplejwt',
    ]
    
    REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (

        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
    }

- urls
    from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
    urlpatterns = [

        path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), // login
        path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    ]

response :

    {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1ODM2MDA5NSwiaWF0IjoxNjU4MjczNjk1LCJqdGkiOiJjYWZhMGE4MGFjODI0N2JmOWM5NjFlODJmZWY1YWUxZSIsInVzZXJfaWQiOjN9.yQLU8zXn5K2s-8i3ErhU2bV35BZzIiBmOdeIRG7Rn2c",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU4MjczOTk1LCJpYXQiOjE2NTgyNzM2OTUsImp0aSI6IjhmYWU3YjEzYmNlNjRiMDU5OTc5YTZkODc4ODgyMTRjIiwidXNlcl9pZCI6M30.W7S3U0xDQpfRQbZ55McO8uX-C5ESJoKap3UxdB68plI"
    }

decode :

    {
    "token_type": "access",
    "exp": 1658273995,
    "iat": 1658273695,
    "jti": "8fae7b13bce64b059979a6d87888214c",
    "user_id": 3
    }

_____________________

to add field to token decode response   




in serilizers.py :
   
    from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

    class NewLoginSerializer(TokenObtainPairSerializer):
        @classmethod
        def get_token(cls, user):
            token = super().get_token(user)
            token['Username'] = user.username
            return token


in views.py :

    from Test.serializers import NewLoginSerializer
    from rest_framework_simplejwt.views import TokenObtainPairView

    class NewLoginView(TokenObtainPairView):
        serializer_class=NewLoginSerializer


in urls.py :
   
    from Test.views import NewLoginView
    urlpatterns = [
        path('api/token/', NewLoginView.as_view(), name='token_obtain_pair'), // login
    ]


decode:
        {
        "token_type": "access",
        "exp": 1658276103,
        "iat": 1658275803,
        "jti": "d729d03e5dfe43dcb589a85e7246e4e9",
        "user_id": 3,
        "first_name": "ali"
        }

________________________________________________________________________________________________________________________

# Registertion in JWT

in settings:
    AUTH_USER_MODEL = 'AppName.User'

in models : 

1- Creat the User model to store the user details ( OverWrite on User Model )
'''
from django.db.models import *
from django.db import transaction
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils import timezone

 
class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
 
    """
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
 
    objects = UserManager()
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
 
    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

'''
2- Create UserManager to control save methods 
'''
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

'''


3- Create Registertion Serializer
'''
class RegisterSerializer(ModelSerializer):
    class Meta:
        model=User
        data_joined = ReadOnlyField()

        fields = ('id', 'email', 'first_name', 'last_name',
                  'data_joined', 'password')
        extra_kwargs = {'password': {'write_only': True}}
'''

4- Create Registertion View 
'''
class RegisterView(APIView):
   def post(self, request):
        user = request.data
        serializer = RegisterSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
'''
