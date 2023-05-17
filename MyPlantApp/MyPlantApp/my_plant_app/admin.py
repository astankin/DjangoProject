from django.contrib import admin

from MyPlantApp.my_plant_app.models import Plant


# Register your models here.
@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    pass
