from django.urls import path

from profile import views

urlpatterns = [
    path('create/', views.profile_create, name='profile-create'),
    path('details/', views.profile_details, name='profile-details'),
    path('edit/', views.profile_edit, name='profile-edit'),
    path('delete/', views.profile_delete, name='profile-delete'),

]