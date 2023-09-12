from django.urls import path
from . import views

urlpatterns = [
    path("", views.UsersListVIew.as_view()),
]
