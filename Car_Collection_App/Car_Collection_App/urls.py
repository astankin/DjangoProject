from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Car_Collection_App.car_app.urls')),
    path('profile/', include('Car_Collection_App.profile_app.urls')),
]
