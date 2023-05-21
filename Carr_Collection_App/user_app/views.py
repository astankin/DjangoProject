from django.shortcuts import render, redirect

from car.models import CarModel
from user_app.forms import ProfileForm, EditProfileForm
from user_app.models import ProfileModel


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
        'form': form
    }
    return render(request, 'profile-create.html', context)


def profile_details(request):
    profile = ProfileModel.objects.first()
    all_cars = CarModel.objects.all()
    total_sum = sum(car.price for car in all_cars)
    context = {'profile': profile, 'total_sum': total_sum}

    return render(request, template_name='profile-details.html', context=context)


def profile_edit(request):
    profile = ProfileModel.objects.first()

    if request.method == "GET":
        context = {'form': EditProfileForm(initial=profile.__dict__)}
        return render(request, 'profile-edit.html', context)
    else:
        form = EditProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('profile-details')
        else:
            context = {
                'profile': ProfileModel.objects.first(),
                'form': form
            }
            return render(request, 'profile-edit.html', context)


def profile_delete(request):
    profile = ProfileModel.objects.first()
    cars = CarModel.objects.all()
    if request.method == 'POST':
        profile.delete()
        cars.delete()
        return redirect('home-page')
    return render(request, 'profile-delete.html', {"profile": ProfileModel.objects.first()})
