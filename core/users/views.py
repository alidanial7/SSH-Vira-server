from django.shortcuts import render
from . import serializers
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.response import Response
import json
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from django.contrib.auth.models import Group, Permission
from .serializers import *
import rest_framework.permissions
from rest_framework.decorators import action

# Create your views here.
from . import models


class UserList(generics.ListAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = UserSerializer


class CustomUserList(viewsets.ModelViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [rest_framework.permissions.IsAdminUser]

    @action(detail=False, methods=['get'], permission_classes=[rest_framework.permissions.IsAuthenticated])
    def my(self, request):
        user = request.user
        user_data = self.serializer_class(user).data
        return JsonResponse(user_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], permission_classes=[])
    def register(self, request):
        username = request.data.get('username')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        is_staff = request.data.get('is_staff')

        user_creator = CustomUser.objects.create_user
        staff_creator = CustomUser.objects.create_staff_user

        if username and password1 and password2 and password1 == password2:

            if is_staff and is_staff == True:
                user_creator = staff_creator

            user = user_creator(
                username=username, password=password1)
            return JsonResponse({'message': 'User created Successfully'}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'message': 'No such user'}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['post'], permission_classes=[])
    def login(self, request):

        username = request.data.get('username')
        password = request.data.get('password')
        if username and password:
            try:
                user = authenticate(username=username, password=password)
                if user is None:
                    return JsonResponse({'message': 'Username or Password is Wrong!'}, status=status.HTTP_401_UNAUTHORIZED)

                token, created = Token.objects.get_or_create(user=user)
                return JsonResponse({'key': token.key}, status=status.HTTP_200_OK)
            except CustomUser.DoesNotExist:
                return JsonResponse({'message': 'No Such User'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return JsonResponse({'message': 'Enter username and password'}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['post'], permission_classes=[])
    def logout(self, request):
        user = request.user
        Token.objects.get(user=user).delete()
        return JsonResponse({'message': 'Log Out Complete :)'}, status=status.HTTP_200_OK)
