from django.shortcuts import render
from rest_framework import generics, status

from .serializers import WorkOutSerializer
from .models import WorkOut


# Create your views here.
class WorkOutListView(generics.ListCreateAPIView):
    queryset = WorkOut.objects.all()
    serializer_class = WorkOutSerializer
