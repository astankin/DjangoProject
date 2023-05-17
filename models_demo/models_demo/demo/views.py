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
            form.save()
            return render(request, 'add.html', {
                'form': EmployeeForm(),
            })
    else:
        form = EmployeeForm()
        return render(request, 'add.html', {
            'form': form
        })


def edit_employee(request, id):
    employee = Employee.objects.get(pk=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return render(request, 'edit_employee.html', {
                'form': form,
                'success': True
            })
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit_employee.html', {
        'form': form
    })


def delete(request, id):
    employee = Employee.objects.get(pk=id)
    if request.method == 'POST':
        employee.delete()
        return render(request, 'delete.html', {
            'employee': employee,
            'success': True
        })
    else:
        return render(request, 'delete.html', {
            'employee': employee
        })