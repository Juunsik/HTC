from rest_framework import generics
from django.shortcuts import render

from .models import User
from .serializers import TinyUserSerializer


# Create your views here.
class UsersListVIew(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = TinyUserSerializer
