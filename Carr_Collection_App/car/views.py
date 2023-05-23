from django.shortcuts import render, redirect

from car.forms import CarCreateForm, CarDeleteForm
from car.models import CarModel
from user_app.models import ProfileModel


# Create your views here.
def catalogue_page(request):
    cars = CarModel.objects.all()
    cars_count = len(cars)
    context = {
        'cars': cars,
        'cars_count': cars_count,
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
        'profile': ProfileModel.objects.first()
    }
    return render(request, 'car-create.html', context)


def car_details(request, id):
    car = CarModel.objects.get(id=id)
    context = {
        'car': car,
        'profile': ProfileModel.objects.first()
    }
    return render(request, 'car-details.html', context)


def car_edit(request, id):
    car = CarModel.objects.get(id=id)
    if request.method == 'POST':
        form = CarCreateForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
        else:
            context = {
                'form': form,
                'profile': ProfileModel.objects.first(),
            }
            return render(request, 'car-edit.html', context)
    else:
        form = CarCreateForm(instance=car)
        context = {
            'form': form,
            'profile': ProfileModel.objects.first(),
            'id': id,
        }
        return render(request, 'car-edit.html', context)


def car_delete(request, id):
    car = CarModel.objects.get(id=id)
    if request.method == 'POST':
        car.delete()
        return redirect('catalogue')
    form = CarDeleteForm(instance=car)
    context = {
        'form': form,
        'profile': ProfileModel.objects.first()
    }
    return render(request, 'car-delete.html', context)
