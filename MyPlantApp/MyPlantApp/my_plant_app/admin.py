from django.contrib import admin

from MyPlantApp.my_plant_app.models import PlantModel


# Register your models here.
@admin.register(PlantModel)
class PlantAdmin(admin.ModelAdmin):
    pass
