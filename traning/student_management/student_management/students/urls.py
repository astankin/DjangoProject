from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/<int:id>', views.view_student, name='view_student'),
    path('search_student/', views.search_student, name='search_student'),
    path('all_students/', views.all_students, name='all_students'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('confirm/<int:id>/', include([
        path('', views.delete, name='delete'),
        path('delete/', views.delete, name='delete')
    ])),
]
