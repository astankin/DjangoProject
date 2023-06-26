from django.urls import path

from ClassBasedViewsDemo.web import views
from ClassBasedViewsDemo.web.views import IndexView, CarsListView, CarDetailsView, CarCreateView, DeleteCarView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', CarCreateView.as_view(), name='create-car'),
    path('dashboard/', CarsListView.as_view(), name='dashboard'),
    path('details/<int:pk>/', CarDetailsView.as_view(), name='details-car'),
    path('delete/<int:pk>/', DeleteCarView.as_view(), name='delete-car'),
]