from django.urls import path

from MyPlantApp.my_plant_app import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('catalogue/', views.show_catalogue, name='catalogue'),
    path('create/', views.create_plant, name='create-plant'),
    path('details/<int:id>', views.plant_details, name='plant-details'),
    path('edit/<int:id>', views.edit_plant, name='edit-plant'),
    path('delete/<int:id>', views.delete_plant, name='delete-plant'),
]