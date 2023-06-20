from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import generic as views
from django.shortcuts import render


# Create your views here.
class UserListView(LoginRequiredMixin, views.ListView):
    model = User
    template_name = 'web/index.html'
