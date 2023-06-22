
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('OnlineLibrary.book_app.urls')),
    path('profile/', include('OnlineLibrary.profile_app.urls')),
]
