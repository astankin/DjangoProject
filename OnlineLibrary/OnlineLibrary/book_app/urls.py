from django.urls import path

from OnlineLibrary.book_app import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('add/', views.add_book, name='add-book'),
    path('edit/<int:id>/', views.edit_book, name='edit-book'),
    path('details/<int:id>/', views.details_book, name='details-book'),
    path('delete/<int:id>/', views.delete_book, name='delete-book'),
]