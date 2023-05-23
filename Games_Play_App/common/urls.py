from django.urls import path

from common import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('dashboard/', views.dashboard, name='dashboard'),
]