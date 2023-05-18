from django.contrib import admin
from authapp.models import ProfileModel
# Register your models here.
@admin.register(ProfileModel)
class UserAdmin(admin.ModelAdmin):
    pass