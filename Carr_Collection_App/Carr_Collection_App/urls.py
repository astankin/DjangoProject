
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('common.urls')),
    path('profile', include('user_app.urls')),
    path('car', include('car.urls')),
]
