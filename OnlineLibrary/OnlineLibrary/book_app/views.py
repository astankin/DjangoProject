from django.shortcuts import render, redirect

from OnlineLibrary.book_app.forms import BookCreateForm
from OnlineLibrary.book_app.models import BookModel
from OnlineLibrary.profile_app.forms import ProfileCreateForm
from OnlineLibrary.profile_app.models import ProfileModel


# Create your views here.
def home_page(request):
    profile = ProfileModel.objects.first()
    books = BookModel.objects.all()
    if profile:
        context = {
            'profile': profile,
            'books': books,
        }
        return render(request, 'home-with-profile.html', context)
    else:
        if request.method == 'POST':
            form = ProfileCreateForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home-page')
        else:
            form = ProfileCreateForm()
        context = {
            'form': form,
            'profile': profile,
            'books': books,
        }
        return render(request, 'home-no-profile.html', context)


def add_book(request):
    if request.method == 'POST':
        form = BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = BookCreateForm()
    context = {
        'form': form,
        'profile': ProfileModel.objects.first()
    }
    return render(request, 'add-book.html', context)


def edit_book(request, id):
    book = BookModel.objects.get(id=id)
    profile = ProfileModel.objects.first()
    if request.method == 'POST':
        form = BookCreateForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = BookCreateForm(instance=book)
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'edit-book.html', context)


def delete_book(request, id):
    book = BookModel.objects.get(id=id)
    book.delete()
    return redirect('home-page')


def details_book(request, id):
    book = BookModel.objects.get(id=id)
    context = {
        'book': book
    }
    return render(request, 'book-details.html', context)
