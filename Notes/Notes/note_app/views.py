from django.shortcuts import render, redirect

from Notes.note_app.forms import NoteForm, NoteDeleteForm
from Notes.note_app.models import NoteModel
from Notes.profile_app.forms import ProfileForm
from Notes.profile_app.models import ProfileModel


# Create your views here.
def index(request):
    try:
        profile = ProfileModel.objects.all()[0]
        context = {
            'profile': profile,
            'notes': NoteModel.objects.all(),
        }
        return render(request, 'home-with-profile.html', context=context)
    except IndexError:
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
            context = {'form': form}
            return render(request, 'home-no-profile.html', context)
        form = ProfileForm()
        context = {'form': form}
        return render(request, 'home-no-profile.html', context)


def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoteForm()
    context = {
        'form': form
    }
    return render(request, 'note-create.html', context)


def edit_note(request, id):
    note = NoteModel.objects.get(id=id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoteForm(instance=note)
    context = {
        'form': form
    }
    return render(request, 'note-edit.html', context)


def details(request, id):
    note = NoteModel.objects.get(id=id)
    profile = ProfileModel.objects.first()
    context = {
        'note': note,
        'profile': profile
    }
    return render(request, 'note-details.html', context)


def delete_note(request, id):
    note = NoteModel.objects.get(id=id)
    if request.method == 'POST':
        note.delete()
        return redirect('index')
    form = NoteDeleteForm(instance=note)
    context = {
        'form': form,
        'profile': ProfileModel.objects.first()
    }

    return render(request, 'note-delete.html', context)
