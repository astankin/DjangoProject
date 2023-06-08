from django.shortcuts import render, redirect

from Car_Collection_App.profile_app.forms import ProfileForm
from Car_Collection_App.profile_app.models import ProfileModel


# Create your views here.
def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = ProfileForm()
    context = {
        'form': form,
        'profile': ProfileModel.objects.first()
    }
    return render(request, 'profile-create.html', context)


def profile_details(request):
    return render(request, 'profile-details.html')


def profile_edit(request):
    return render(request, 'profile-edit.html')


def profile_delete(request):
    return render(request, 'profile-delete.html')
