from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from account.serializers import UserSerializer
# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):

    serializer = UserSerializer(data = request.data)
    
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()

        # 회원가입과 동시에 로그인 -> 토큰 발급
        token = RefreshToken.for_user(user)
        refresh_token = str(token)
        access_token = str(token.access_token)
        update_last_login(None, user)

        return Response({'refresh_token': refresh_token,
                        'access_token': access_token, 'data' : serializer.data}, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):

    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username = username, password = password)

    if user is not None:
        token = RefreshToken.for_user(user)
        refresh_token = str(token)
        access_token = str(token.access_token)
        update_last_login(None, user)

        return Response({'refresh_token': refresh_token,
                        'access_token': access_token, }, status=status.HTTP_200_OK)
    
    return Response({'message': '아이디 또는 비밀번호가 일치하지 않습니다.'}, status=status.HTTP_401_UNAUTHORIZED)
    