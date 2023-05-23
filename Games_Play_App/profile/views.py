from django.shortcuts import render, redirect

from profile.forms import ProfileForm


# Create your views here.
def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = ProfileForm()
    context = {
        'form': form
    }
    return render(request, 'create-profile.html', context)


def profile_details(request):
    pass


def profile_edit(request):
    pass


def profile_delete(request):
    pass
