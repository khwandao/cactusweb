from django.urls import path
from cactus import views

urlpatterns = [
    path("", views.home, name="home"),
]