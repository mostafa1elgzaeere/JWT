import email
from typing_extensions import Required
from Test.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import *

class RegisterSerializer(ModelSerializer):
    class Meta:
        model=User
        data_joined = ReadOnlyField()
        password=CharField(write_only=True,required=True)

        fields = ('id', 'email', 'first_name', 'last_name',
                  'data_joined', 'password')
    
    def create(self, validated_data):
        user=User.objects.create_user(
        email=validated_data['email'],
        password=validated_data['password']
        )
        return user
        
        
         
class NewLoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['first_name'] = user.first_name
        # ...

        return token
