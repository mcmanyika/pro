from django.urls import path
from django.contrib import admin
from joins.views import *
from libs.views import *

urlpatterns = [
    path("", register_view, name="login"),
    path(
        "register-user-attributes/",
        RegisterUserAttributes,
        name="register-user-attributes",
    ),
    path("logout/", Logout, name="logout"),
    path("password/", change_password, name="change_password"),
    path("signup/", signup, name="signup"),
    path("signup-confirmation/", signup_confirmation, name="signup-confirmation"),
    path("user-img/", user_img, name="user-img"),
]
