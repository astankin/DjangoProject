from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/<int:id>', views.view_student, name='view_student'),
    path('search_student/', views.search_student, name='search_student'),
    path('all_students/', views.all_students, name='all_students'),
    path('add/', views.add, name='add'),
]
