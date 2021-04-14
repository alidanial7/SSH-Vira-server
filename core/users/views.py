from django.shortcuts import render
from . import serializers
from rest_framework import generics

# Create your views here.
from . import models


class UserList(generics.ListAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
