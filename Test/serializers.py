from  rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class NewLoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['first_name'] = user.username
        # ...

        return token