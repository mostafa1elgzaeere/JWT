from Test.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import *

class RegisterSerializer(ModelSerializer):
    class Meta:
        model=User
        data_joined = ReadOnlyField()

        fields = ('id', 'email', 'first_name', 'last_name',
                  'data_joined', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class NewLoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['first_name'] = user.first_name
        # ...

        return token
