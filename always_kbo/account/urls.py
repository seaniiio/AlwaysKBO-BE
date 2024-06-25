from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.signup),
    path('login', views.login),
    path('<int:pk>', views.UserApiView.as_view())
]