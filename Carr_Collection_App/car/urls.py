from django.urls import path, include

from car import views

urlpatterns = [
    path('catalogue/', views.catalogue_page, name='catalogue'),
    path('create/', views.car_create, name='car-create'),
    path('/<int:id>/details/', views.car_details, name='car-details'),
    path('/<int:id>/edit/', views.car_edit, name='car-edit'),
    path('/<int:id>/delete/', views.car_delete, name='car-delete'),
]
