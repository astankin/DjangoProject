from django.urls import path

from Notes.note_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.create_note, name='create-note'),
    path('edit/<int:id>/', views.edit_note, name='edit-note'),
    path('details/<int:id>/', views.details, name='details'),
    path('delete/<int:id>/', views.delete_note, name='delete-note'),
]
