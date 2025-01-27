from django.urls import path

from books_api.views import ListBookView

urlpatterns = [
    path('books/', ListBookView.as_view(), name='books'),
    # path('books/<int:pk>/', DetailBookView.as_view()),

]