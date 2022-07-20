from rest_framework.response import Response
from Test.serializers import NewLoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class NewLoginView(TokenObtainPairView):
    serializer_class=NewLoginSerializer
