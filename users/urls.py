from django.urls import path
from . import views

urlpatterns = [
    path("", views.UserList.as_view()),
    path("me", views.Me.as_view()),
    path("@<str:username>", views.UserDetail.as_view()),
    path("change-password", views.ChangePassword.as_view()),
    path("sign-up", views.SignUp.as_view()),
    path("log-in", views.LogIn.as_view()),
    path("log-out", views.LogOut.as_view()),
]
