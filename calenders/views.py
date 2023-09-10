from django.shortcuts import render
from rest_framework import generics, status

from .serializers import CalenderSerializer
from .models import Calender


# Create your views here.
class CalenderListView(generics.ListCreateAPIView):
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer
