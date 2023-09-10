from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination

from .serializers import CalenderSerializer
from .models import Calender


# Create your views here.
class CalenderPageNumberPagination(PageNumberPagination):
    page_size = 7


class CalenderListView(generics.ListCreateAPIView):
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer
    pagination_class = CalenderPageNumberPagination


class CalenderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer
    lookup_field = "created_at"
