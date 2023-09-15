from django.urls import path
from . import views

urlpatterns = [
    path("<int:users_id>", views.CalenderListView.as_view()),
    path("<int:users_id>/<str:created_at>", views.CalenderDetailView.as_view()),
]
