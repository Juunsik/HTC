from django.urls import path
from . import views

urlpatterns = [
    path("", views.CalenderListView.as_view()),
    path("@<str:created_at>", views.CalenderDetailView.as_view()),
]
