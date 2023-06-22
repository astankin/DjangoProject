from django.shortcuts import render, redirect

from Exam_Preparation.album.models import AlbumModel
from Exam_Preparation.profile_app.models import ProfileModel


# Create your views here.
def profile_details(request):
    profile = ProfileModel.objects.first()
    albums_count = len(AlbumModel.objects.all())
    context = {
        'profile': profile,
        'albums_count': albums_count,
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
