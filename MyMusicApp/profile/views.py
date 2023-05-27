from django.shortcuts import render, redirect

from album.models import AlbumModel
from profile.models import ProfileModel


# Create your views here.

def profile_details(request):
    profile = ProfileModel.objects.first()
    all_albums = len(AlbumModel.objects.all())
    context = {
        'profile': profile,
        'all_albums': all_albums,
    }
    return render(request, 'profile-details.html', context)


def profile_delete(request):
    profile = ProfileModel.objects.first()
    albums = AlbumModel.objects.all()
    if request.method == 'POST':
        profile.delete()
        albums.delete()
        return redirect('home-page')
    return render(request, 'profile-delete.html')