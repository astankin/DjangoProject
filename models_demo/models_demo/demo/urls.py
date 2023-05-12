from django.urls import path

from models_demo.demo import views

urlpatterns = [
    path('', views.get_all_employees, name='index')
]