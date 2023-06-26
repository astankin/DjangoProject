
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('Exam_Preparation.profile_app.urls')),
    path('', include('Exam_Preparation.album.urls')),
]
