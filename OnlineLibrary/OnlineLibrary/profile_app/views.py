from django.shortcuts import render, redirect

from OnlineLibrary.book_app.models import BookModel
from OnlineLibrary.profile_app.forms import ProfileCreateForm, ProfileDeleteForm
from OnlineLibrary.profile_app.models import ProfileModel


# Create your views here.
def profile_details(request):
    profile = ProfileModel.objects.first()
    context = {
        'profile': profile
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = ProfileModel.objects.first()
    if request.method == 'POST':
        form = ProfileCreateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-details')
    else:
        form = ProfileCreateForm(instance=profile)
    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = ProfileModel.objects.first()
    books = BookModel.objects.all()
    if request.method == 'POST':
        profile.delete()
        books.delete()
        return redirect('home-page')
    form = ProfileDeleteForm(instance=profile)
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'delete-profile.html', context)
