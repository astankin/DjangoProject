from django.shortcuts import render, redirect

from Car_Collection_App.car_app.forms import CarCreateForm, CarDeleteForm
from Car_Collection_App.car_app.models import CarModel
from Car_Collection_App.profile_app.models import ProfileModel


# Create your views here.
def index(request):
    profile = ProfileModel.objects.first()
    context = {
        'profile': profile
    }
    return render(request, 'index.html', context)


def catalogue(request):
    cars = CarModel.objects.all()
    context = {
        'cars': cars,
        'profile': ProfileModel.objects.first(),
    }
    return render(request, 'catalogue.html', context)


def car_create(request):
    if request.method == 'POST':
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CarCreateForm()
    context = {
        'form': form,
        'profile': ProfileModel.objects.first(),
    }
    return render(request, 'car-create.html', context)


def car_details(request, id):
    car = CarModel.objects.get(id=id)
    content = {
        'car': car,
        'profile': ProfileModel.objects.first(),
    }
    return render(request, 'car-details.html', content)


def car_edit(request, id):
    car = CarModel.objects.get(id=id)
    if request.method == 'POST':
        form = CarCreateForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CarCreateForm(instance=car)
    context = {
        'form': form,
        'profile': ProfileModel.objects.first(),
    }
    return render(request, 'car-edit.html', context)


def car_delete(request, id):
    car = CarModel.objects.get(id=id)
    if request.method == 'POST':
        car.delete()
        return redirect('catalogue')
    else:
        form = CarDeleteForm(instance=car)
    context = {
        'form': form,
        'profile': ProfileModel.objects.first(),
    }
    return render(request, 'car-delete.html', context)