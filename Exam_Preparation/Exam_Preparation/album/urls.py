from django.urls import path, include

from Exam_Preparation.album import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('album/', include([
        path('add/', views.add_album, name='add-album'),
        path('details/<int:id>', views.album_details, name='album-details'),
        path('edit/<int:id>', views.album_edit, name='album-edit'),
        path('delete/<int:id>', views.album_delete, name='album-delete'),
    ])),
]