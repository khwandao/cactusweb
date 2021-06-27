from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'cactus'

urlpatterns = [
    path("", views.home, name="home"),
    path('species/<int:species_id>/', views.detail),
    
    path('cacti_detail/<int:cactus_id>/', views.cacti_detail),

    path('cactus_page/', views.cactus_page),

    path('chart/', views.chart),
]
