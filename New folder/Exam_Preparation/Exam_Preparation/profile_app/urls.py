from django.urls import path

from Exam_Preparation.profile_app import views

urlpatterns = [
    path('details/', views.profile_details, name='profile-details'),
    path('delete/', views.profile_delete, name='profile-delete'),
]