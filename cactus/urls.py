from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'cactus'

urlpatterns = [
    path("", views.home, name="home"),
    path('<int:species_id>/', views.detail),
]
