from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination

from .serializers import WorkOutSerializer
from .models import WorkOut


# Create your views here.
class WorkOutPageNumberPagination(PageNumberPagination):
    page_size = 5


class WorkOutListView(generics.ListCreateAPIView):
    queryset = WorkOut.objects.all()
    serializer_class = WorkOutSerializer


class WorkOutDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkOut.objects.all()
    serializer_class = WorkOutSerializer
