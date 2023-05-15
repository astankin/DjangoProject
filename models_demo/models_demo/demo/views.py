from django.shortcuts import render, redirect

from models_demo.demo.forms import EmployeeForm
from models_demo.demo.models import Department, Employee


# Create your views here.
def show_all_employees(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees,
    }

    return render(request, 'department.html', context)


def index(request):
    return render(request, 'index.html')


def back(request):
    return redirect('index.html')


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            projects = form.cleaned_data.pop('projects')
            employee = Employee.objects.create(
                **form.cleaned_data
            )
            employee.projects.set(projects)
            employee.save()
            return render(request, 'add.html', {
                'form': EmployeeForm(),
            })
    else:
        form = EmployeeForm()
        return render(request, 'add.html', {
            'form': form
        })
