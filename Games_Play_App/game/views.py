from django.shortcuts import render, redirect

from game.forms import GameForm, GameDeleteForm
from game.models import GameModel
from profile.models import ProfileModel


# Create your views here.


def create_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = GameForm()
    context = {
        'form': form,
        'profile': ProfileModel.objects.first(),
    }
    return render(request, 'create-game.html', context)


def game_details(request, id):
    game = GameModel.objects.get(id=id)
    context = {
        'game': game,
        'profile': ProfileModel.objects.first(),
    }
    return render(request, 'details-game.html', context)


def edit_game(request, id):
    game = GameModel.objects.get(id=id)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = GameForm(instance=game)
    context = {
        'form': form,
        'profile': ProfileModel.objects.first(),
    }
    return render(request, 'edit-game.html', context)


def delete_game(request, id):
    game = GameModel.objects.get(id=id)
    if request.method == 'POST':
        game.delete()
        return redirect('dashboard')
    form = GameDeleteForm(instance=game)
    context = {
        'form': form,
        'profile': ProfileModel.objects.first()
    }
    return render(request, 'delete-game.html', context)
