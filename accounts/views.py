

from django.shortcuts import render
from requests import Response

from rest_framework import generics, permissions, status, response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .models import MyUser
from .serializers import CustomUserSerializer, LoginSerializer


class UserCreate(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (permissions.AllowAny,)

class UserList(generics.ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class = CustomUserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = CustomUserSerializer

class LoginAPIView(APIView):
    permission_classes = [AllowAny,]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors)



