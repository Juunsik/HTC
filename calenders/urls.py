from django.urls import path
from . import views

urlpatterns = [
    path("", views.CalenderListView.as_view()),
]