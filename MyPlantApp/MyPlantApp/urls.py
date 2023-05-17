
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MyPlantApp.my_plant_app.urls')),
    path('profile/', include('MyPlantApp.authapp.urls')),
]
