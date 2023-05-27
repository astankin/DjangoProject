from django.shortcuts import render, redirect

from album.forms import AlbumCreateForm, AlbumDeleteForm
from album.models import AlbumModel
from profile.models import ProfileModel


# Create your views here.
def add_album(request):
    profile = ProfileModel.objects.first()
    if request.method == 'POST':
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = AlbumCreateForm()
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'add-album.html', context)


def album_details(request, id):
    album = AlbumModel.objects.get(id=id)
    context = {
        'album': album
    }
    return render(request, 'album-details.html', context)


def edit_album(request, id):
    album = AlbumModel.objects.get(id=id)
    profile = ProfileModel.objects.first()
    if request.method == 'POST':
        form = AlbumCreateForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = AlbumCreateForm(instance=album)
    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'edit-album.html', context)


def delete_album(request, id):
    album = AlbumModel.objects.get(id=id)
    profile = ProfileModel.objects.first()
    if request.method == 'POST':
        album.delete()
        return redirect('home-page')
    form = AlbumDeleteForm(instance=album)
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'delete-album.html', context)
