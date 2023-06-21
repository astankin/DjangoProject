from django.shortcuts import render, redirect

from exam_prep1.plant_app.models import PlantModel
from exam_prep1.profile_app.forms import ProfileCreateForm, ProfileEditForm
from exam_prep1.profile_app.models import ProfileModel


# Create your views here.
def create_profile(request):
    if request.method == 'POST':
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = ProfileCreateForm()
    context = {
        'profile': ProfileModel.objects.first(),
        'form': form
    }
    return render(request, 'create-profile.html', context)


def details_profile(request):
    profile = ProfileModel.objects.first()
    plants_count = len(PlantModel.objects.all())
    context = {
        'profile': profile,
        'plants_count': plants_count,
    }
    return render(request, 'profile-details.html', context)


def edit_profile(request):
    profile = ProfileModel.objects.first()
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details-profile')
    else:
        form = ProfileEditForm(instance=profile)
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = ProfileModel.objects.first()
    plants = PlantModel.objects.all()
    if request.method == 'POST':
        profile.delete()
        plants.delete()
        return redirect('home')
    return render(request, 'delete-profile.html')
