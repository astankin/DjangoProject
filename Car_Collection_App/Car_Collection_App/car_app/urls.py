from django.urls import path, include

from Car_Collection_App.car_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('car/', include([
        path('create/', views.car_create, name='car-create'),
        path('<int:id>/details/', views.car_details, name='car-details'),
        path('<int:id>/edit/', views.car_edit, name='car-edit'),
        path('<int:id>/delete/', views.car_delete, name='car-delete'),
    ])),
]