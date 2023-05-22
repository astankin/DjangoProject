from django.shortcuts import render

from user_app.models import ProfileModel


# Create your views here.
def home_page(request):
    profile = ProfileModel.objects.first()
    context = {
        'profile': profile
    }
    return render(request, 'index.html', context)
