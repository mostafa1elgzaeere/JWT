# Authntication with JWT #

''' Login '''

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
