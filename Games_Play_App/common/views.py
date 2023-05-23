from django.shortcuts import render
from game.models import GameModel
from profile.models import ProfileModel


# Create your views here.
def home_page(request):
    profile = ProfileModel.objects.first()
    context = {
        'profile': profile
    }
    return render(request, 'home-page.html', context)


# Create your views here.
def dashboard(request):
    profile = ProfileModel.objects.first()
    games = GameModel.objects.all()
    context = {
        'profile': profile,
        'games': games
    }
    return render(request, 'dashboard.html', context)
