from django.urls import path

from OnlineLibrary.profile_app import views

urlpatterns = [
    path('', views.profile_details, name='profile-details'),
    path('edit/', views.edit_profile, name='edit-profile'),
    path('delete/', views.delete_profile, name='delete-profile'),
]