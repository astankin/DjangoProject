from django.shortcuts import render, redirect

from Car_Collection_App.car_app.models import CarModel
from Car_Collection_App.profile_app.forms import ProfileForm, ProfileEditForm
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
    profile = ProfileModel.objects.first()
    cars = CarModel.objects.all()
    total_price = sum([car.price for car in cars])
    context = {
        'profile': profile,
        'total_price': total_price,

    }
    return render(request, 'profile-details.html', context)


def profile_edit(request):
    profile = ProfileModel.objects.first()
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-details')
    else:
        form = ProfileEditForm(instance=profile)
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'profile-edit.html', context)


def profile_delete(request):
    profile = ProfileModel.objects.first()
    cars = CarModel.objects.all()
    if request.method == 'POST':
        profile.delete()
        cars.delete()
        return redirect('index')
    return render(request, 'profile-delete.html')
