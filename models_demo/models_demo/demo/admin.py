from django.contrib import admin

from models_demo.demo.models import Department, Employee, Project


# Register your models here.
@admin.register(Employee, Department, Project)
class DemoAdmin(admin.ModelAdmin):
    pass
