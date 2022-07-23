from rest_framework.response import Response 
from Test.serializers import NewLoginSerializer, RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

class RegisterView(CreateAPIView):
    serializer_class=RegisterSerializer
#    def post(self, request):
#         user = request.data
#         serializer = RegisterSerializer(data=user)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
class NewLoginView(TokenObtainPairView):
    serializer_class=NewLoginSerializer
