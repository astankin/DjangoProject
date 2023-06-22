from django.shortcuts import render, redirect

from Exam_Preparation.album.forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from Exam_Preparation.album.models import AlbumModel
from Exam_Preparation.profile_app.forms import CreateProfileForm
from Exam_Preparation.profile_app.models import ProfileModel


# Create your views here.
def home(request):
    profile = ProfileModel.objects.first()
    if profile:
        context = {
            'profile': profile,
            'albums': AlbumModel.objects.all(),
        }
        return render(request, 'home-with-profile.html', context=context)
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
        context = {
            'form': form,
            'profile': profile,
        }
        return render(request, 'home-no-profile.html', context)
    form = CreateProfileForm()
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'home-no-profile.html', context)


def add_album(request):
    if request.method == 'POST':
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = AlbumCreateForm()
    context = {
        'form': form,
        'profile': ProfileModel.objects.first()
    }
    return render(request, 'add-album.html', context)


def album_details(request, id):
    album = AlbumModel.objects.get(id=id)
    context = {
        'album': album,
        'profile': ProfileModel.objects.first(),
    }
    return render(request, 'album-details.html', context)


def album_edit(request, id):
    album = AlbumModel.objects.get(id=id)
    if request.method == 'POST':
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = AlbumEditForm(instance=album)
    context = {
        'form': form,
        'profile': ProfileModel.objects.first(),
    }
    return render(request, 'edit-album.html', context)


def album_delete(request, id):
    album = AlbumModel.objects.get(id=id)
    if request.method == 'POST':
        album.delete()
        return redirect('home-page')
    else:
        form = AlbumDeleteForm(instance=album)
    context = {
        'form': form,
        'profile': ProfileModel.objects.first(),
    }
    return render(request, 'delete-album.html', context)
