from django.shortcuts import render

from models_demo.demo.models import Employee


# Create your views here.

def get_all_employees(request):
    context = {
        'employees': Employee.objects.all()
    }
    return render(request, 'index.html', context)
