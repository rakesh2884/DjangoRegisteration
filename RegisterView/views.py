from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from .serializers import UserProfileSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class register(APIView):
    serializer_class = UserProfileSerializer

    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(password=make_password(request.data['password']))
            return Response("Register Successfull",
                            201)
        return Response(serializer.errors, 400)


class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')     
        user = User.objects.get(username=username)
        if check_password(password, user.password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'access_token': str(refresh.access_token)
            }, 201)
        else:
            return Response("Invalid Password", 400)
