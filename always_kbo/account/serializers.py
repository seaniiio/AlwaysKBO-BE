from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'name', 'age', 'gender', 'team')

# 사용자 정보 확인에 필요한 필드만 정의
class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'name', 'age', 'gender', 'team')