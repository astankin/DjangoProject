from django.shortcuts import render, redirect

from exam_prep1.plant_app.forms import PlantCreateForm, PlantDeleteForm
from exam_prep1.plant_app.models import PlantModel
from exam_prep1.profile_app.models import ProfileModel


# Create your views here.
def home(request):
    profile = ProfileModel.objects.first()
    context = {
        'profile': profile
    }
    return render(request, 'home-page.html', context)


def create_plant(request):
    profile = ProfileModel.objects.first()
    if request.method == 'POST':
        form = PlantCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = PlantCreateForm()
    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'create-plant.html', context)


def details_plant(request, id):
    profile = ProfileModel.objects.first()
    plant = PlantModel.objects.get(id=id)
    context = {
        'profile': profile,
        'plant': plant,
    }
    return render(request, 'plant-details.html', context)


def edit_plant(request, id):
    profile = ProfileModel.objects.first()
    plant = PlantModel.objects.get(id=id)
    if request.method == 'POST':
        form = PlantCreateForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = PlantCreateForm(instance=plant)
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'edit-plant.html', context)


def catalogue(request):
    profile = ProfileModel.objects.first()
    plants = PlantModel.objects.all()
    context = {
        'profile': profile,
        'plants': plants
    }
    return render(request, 'catalogue.html', context)


def delete_plant(request, id):
    profile = ProfileModel.objects.first()
    plant = PlantModel.objects.get(id=id)
    if request.method == 'POST':
        plant.delete()
        return redirect('catalogue')
    else:
        form = PlantDeleteForm(instance=plant)
    context = {
        'profile': profile,
        'plant': plant,
        'form': form,
    }
    return render(request, 'delete-plant.html', context)
