from django.contrib import admin

from MyPlantApp.authapp.models import Profile


# Register your models here.

@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    pass
