from django.urls import path
from . import views

urlpatterns = [
    path("", views.WorkOutListView.as_view()),
    path("@<int:pk>", views.WorkOutDetailView.as_view()),
]
