from django.shortcuts import render, redirect

from game.models import GameModel
from profile.forms import ProfileForm, ProfileEditForm
from profile.models import ProfileModel


# Create your views here.
def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = ProfileForm()
    context = {
        'form': form
    }
    return render(request, 'create-profile.html', context)


def profile_details(request):
    profile = ProfileModel.objects.first()
    games = GameModel.objects.all()
    games_count = len(games)
    average_rating = sum([game.rating for game in games]) / games_count
    context = {
        'profile': profile,
        'games_count': games_count,
        'average_rating': average_rating,
    }
    return render(request, 'details-profile.html', context)


def profile_edit(request):
    profile = ProfileModel.objects.first()
    if request.method == "GET":
        context = {'form': ProfileEditForm(initial=profile.__dict__)}
        return render(request, 'edit-profile.html', context)
    else:
        form = ProfileEditForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('profile-details')
        else:
            context = {
                'profile': ProfileModel.objects.first(),
                'form': form
            }
            return render(request, 'edit-profile.html', context)


def profile_delete(request):
    profile = ProfileModel.objects.first()
    games = GameModel.objects.all()
    if request.method == 'POST':
        profile.delete()
        games.delete()
        return redirect('home-page')
    return render(request, 'delete-profile.html')
