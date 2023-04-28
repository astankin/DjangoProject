from django.contrib import admin
from .models import Student

# Register your models here.

# admin.site.register(Student)

@admin.register(Student)
class SdudentAdmin(admin.ModelAdmin):
    list_display = ("id", "student_number", "first_name", "last_name")