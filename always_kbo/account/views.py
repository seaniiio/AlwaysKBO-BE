from django.shortcuts import render
from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from account.serializers import UserSerializer
# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):

    serializer = UserSerializer(data = request.data)
    
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.save()

        # 회원가입과 동시에 로그인 -> 토큰 발급
        token = TokenObtainPairSerializer.get_token(user)
        refresh_token = str(token)
        access_token = str(token.access_token)

        return Response({'refresh_token' : str(refresh_token), 'access_token' : str(access_token), 'data' : serializer.data}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

