from django.urls import path

from photo import views

urlpatterns = [
    path('', views.index, name='index')
]