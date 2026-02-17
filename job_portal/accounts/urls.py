from django.urls import path
from .views import register, UserLoginView, UserLogoutView
from . import views

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/", views.profile_view, name="profile"),

]
