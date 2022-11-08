from django.urls import path
from . import views


urlpatterns = [
    path("", views.mainpage_request, name="homepage"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("mainpage/", views.mainpage_request, name="mainpage") 




]