from django.shortcuts import render, redirect

from GameAppTraning.web.forms import ProfileCreateForm, GameCreateForm
from GameAppTraning.web.models import ProfileModel, GameModel


# Create your views here.
def home_page(request):
    profile = ProfileModel.objects.first()
    context = {
        'profile': profile
    }
    return render(request, 'home-page.html', context)


def dashboard(request):
    profile = ProfileModel.objects.first()
    games = GameModel.objects.all()
    context = {
        'profile': profile,
        'games': games,
    }
    return render(request, 'dashboard.html', context)


def create_profile(request):
    profile = ProfileModel.objects.first()
    if request.method == 'POST':
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = ProfileCreateForm()
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'create-profile.html', context)


def edit_profile(request):
    return render(request, 'edit-profile.html')


def details_profile(request):
    return render(request, 'details-profile.html')


def delete_profile(request):
    return render(request, 'delete-profile.html')


def create_game(request):
    profile = ProfileModel.objects.first()
    if request.method == 'POST':
        form = GameCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = GameCreateForm()
    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'create-game.html', context)


def details_game(request):
    return render(request, 'details-game.html')


def edit_game(request):
    return render(request, 'edit-game.html')


def delete_game(request):
    return render(request, 'delete-game.html')
