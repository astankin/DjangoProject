from django.urls import path

from exam_prep1.plant_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cataloque/', views.catalogue, name='catalogue'),
    path('create/', views.create_plant, name='create-plant'),
    path('details/<int:id>/', views.details_plant, name='details-plant'),
    path('edit/<int:id>/', views.edit_plant, name='edit-plant'),
    path('delete/<int:id>/', views.delete_plant, name='delete-plant'),
]

