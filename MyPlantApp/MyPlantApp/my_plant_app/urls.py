from django.urls import path

from MyPlantApp.my_plant_app import views

urlpatterns = [
    path('', views.home_page, name='home-page')
]