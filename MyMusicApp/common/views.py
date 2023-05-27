from django.shortcuts import render, redirect

from album.models import AlbumModel
from profile.forms import CreateProfileForm
from profile.models import ProfileModel


# Create your views here.
def home_page(request):
    try:
        profile = ProfileModel.objects.all()[0]
        context = {
            'profile': profile,
            'albums': AlbumModel.objects.all(),
        }
        return render(request, 'home-with-profile.html', context=context)
    except IndexError:
        if request.method == 'POST':
            form = CreateProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home-page')
            context = {'form': form}
            return render(request, 'home-no-profile.html', context)
        form = CreateProfileForm()
        context = {'form': form}
        return render(request, 'home-no-profile.html', context)
