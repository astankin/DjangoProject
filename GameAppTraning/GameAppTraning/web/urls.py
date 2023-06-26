from django.urls import path, include

from GameAppTraning.web import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('profile', include([
        path('create/', views.create_profile, name='create-profile'),
        path('edit/', views.edit_profile, name='edit-profile'),
        path('delete/', views.delete_profile, name='delete-profile'),
        path('details/', views.details_profile, name='details-profile'),
    ])),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('game/', include([
        path('create/', views.create_game, name='create-game'),
        path('details/<int:id>', views.details_game, name='details-game'),
        path('edit/<int:id>', views.edit_game, name='edit-game'),
        path('delete/<int:id>', views.delete_game, name='delete-game'),
    ]))
]