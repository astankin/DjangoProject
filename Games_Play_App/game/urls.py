from django.urls import path, include

from game import views

urlpatterns = [
    path('game/', include([
        path('create/', views.create_game, name='create-game'),
        path('details/<int:id>', views.game_details, name='game-details'),
        path('edit/<int:id>', views.edit_game, name='edit_game'),
        path('delete/<int:id>', views.delete_game, name='delete-game'),

    ]))
]