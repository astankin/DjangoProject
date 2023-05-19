from django.shortcuts import render, redirect

from MyPlantApp.authapp.forms import ProfileForm, EditProfileForm
from MyPlantApp.authapp.models import ProfileModel
from MyPlantApp.my_plant_app.models import PlantModel


# Create your views here.
def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = ProfileForm()

    context = {
        'form': form
    }
    return render(request, 'create-profile.html', context=context)


def profile_details(request):
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
        form = EditProfileForm(request.POST, instance=profile)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('profile-details')
    else:
        form = EditProfileForm(instance=profile)
        context = {
            'form': form
        }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = ProfileModel.objects.first()
    plants = PlantModel.objects.all()
    if request.method == 'POST':
        profile.delete()
        plants.delete()
        return redirect('home-page')
    return render(request, 'delete-profile.html')
