from django.urls import path

from auth_demo.web.views import UserListView

urlpatterns = [
    path('', UserListView.as_view(), name='index')
]