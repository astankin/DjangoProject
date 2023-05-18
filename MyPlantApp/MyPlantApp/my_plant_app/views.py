from django.shortcuts import render, redirect

from MyPlantApp.authapp.models import ProfileModel
from MyPlantApp.my_plant_app import models
from MyPlantApp.my_plant_app.forms import PlantForm, DeletePlantForm
from MyPlantApp.my_plant_app.models import PlantModel


# Create your views here.
def home_page(request):
    profile = ProfileModel.objects.first()
    context = {
        'profile': profile
    }
    return render(request, 'home-page.html', context)


def show_catalogue(request):
    plants = models.PlantModel.objects.all()
    context = {'plants': plants}
    return render(request, 'catalogue.html', context)


def create_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = PlantForm()
    context = {
        'form': form
    }
    return render(request, 'create-plant.html', context)


def plant_details(request, id):
    plant = PlantModel.objects.get(id=id)
    context = {
        'plant': plant
    }
    return render(request, 'plant-details.html', context)


def edit_plant(request, id):
    plant = PlantModel.objects.get(id=id)

    if request.method == 'POST':
        form = PlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
        else:
            context = {'form': form}
            return render(request, 'edit-plant.html', context)
    else:
        form = PlantForm(instance=plant)
        context = {'form': form}
        return render(request, 'edit-plant.html', context)


def delete_plant(request, id):
    plant = PlantModel.objects.get(id=id)
    if request.method == 'POST':
        plant.delete()
        return redirect('catalogue')
    form = DeletePlantForm(instance=plant)
    context = {'form': form}

    return render(request, 'delete-plant.html', context)
