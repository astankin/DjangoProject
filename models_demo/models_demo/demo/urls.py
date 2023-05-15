from django.urls import path

from models_demo.demo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employees/', views.show_all_employees, name='show-all-employees'),
    path('add/', views.add_employee, name='add-employee'),
]