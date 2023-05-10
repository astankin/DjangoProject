from django.contrib import admin

from models_demo.demo.models import Employee, Departments, Project


# Register your models here.
@admin.register(Employee, Departments, Project)
class DemoAdmin(admin.ModelAdmin):
    pass
