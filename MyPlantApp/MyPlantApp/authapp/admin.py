from django.contrib import admin

from MyPlantApp.authapp.models import ProfileModel


# Register your models here.

@admin.register(ProfileModel)
class UserAdmin(admin.ModelAdmin):
    pass
