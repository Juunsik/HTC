from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination

from .serializers import CalenderSerializer
from .models import Calender
from users.models import User


# Create your views here.
class CalenderPageNumberPagination(PageNumberPagination):
    page_size = 7


class CalenderListView(generics.ListCreateAPIView):
    # queryset = Calender.objects.all()
    # lookup_field = "users_id"
    serializer_class = CalenderSerializer
    pagination_class = CalenderPageNumberPagination

    def get_queryset(self):
        return Calender.objects.filter(users_id=self.kwargs["users_id"])


class CalenderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CalenderSerializer
    lookup_field = "created_at"

    def get_user(self):
        return get_object_or_404(User.objects.all(), id=self.kwargs["users_id"])

    def get_queryset(self):
        user = self.get_user()
        return Calender.objects.filter(users_id=user)
