from django.shortcuts import render, redirect

from Notes.note_app.models import NoteModel
from Notes.profile_app.models import ProfileModel


# Create your views here.
def profile_details(request):
    profile = ProfileModel.objects.first()
    notes_count = len(NoteModel.objects.all())
    context = {
        'profile': profile,
        'notes_count': notes_count,
    }
    return render(request, 'profile.html', context)


def delete_profile(request):
    profile = ProfileModel.objects.first()
    notes = NoteModel.objects.all()
    notes.delete()
    profile.delete()
    return redirect('index')