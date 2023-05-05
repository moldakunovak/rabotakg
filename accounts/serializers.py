from rest_framework import serializers
from .models import MyUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = MyUser(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(min_length=6, write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        username = attrs.get('email')
        password = attrs.get('password')
        if username is None:
            raise serializers.ValidationError('Username is required')

        if password is None:
            raise serializers.ValidationError('Password is required')

        return attrs

    def create(self, validated_data):
        username = validated_data.get('email')
        password = validated_data.get('password')
        user = MyUser.objects.get(username=username, password=password)
        if user is None:
            raise serializers.ValidationError('User not found')
        if not user.is_active:
            raise serializers.ValidationError('User not active')
        token_key, _ = Token.objects.get_or_create(user=user)

        return {
            "token": token_key
            }
