from django.contrib.auth.views import LoginView
from django.urls import path

from auth_demo.auth_app import views
from auth_demo.auth_app.views import SignUpView, SignInView

urlpatterns = [
    # path('', views.index, name='index-page'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
]