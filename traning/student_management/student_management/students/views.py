from django.shortcuts import render
from .models import Student
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'index.html', {
        'students': Student.objects.all()
    })

def view_student(request, id):
    student = Student.objects.get(pk=id)
    return render(request, 'view_student.html', {
        'student': student
    })

def search_student(request):
    if request.method == "POST":
        searched = request.POST['searched']
        students = Student.objects.filter(first_name__contains=searched)
        return render(request, 'search_student.html', 
        {'searched': searched,
         'students': students})
    else:
        return render(request, 'search_student.html', 
        {})
