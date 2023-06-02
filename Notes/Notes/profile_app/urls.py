from django.urls import path

from Notes.profile_app import views

urlpatterns = [
    path('', views.profile_details, name='profile'),
    path('delete/', views.delete_profile, name='delete-profile')
]