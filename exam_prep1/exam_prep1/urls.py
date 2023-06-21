
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('exam_prep1.plant_app.urls')),
    path('profile/', include('exam_prep1.profile_app.urls')),
]
