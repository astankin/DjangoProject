from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class GameBaseModel(models.Model):
    GAME_CATEGORIES = [
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Puzzle', 'Puzzle'),
        ('Strategy', 'Strategy'),
        ('Sports', 'Sports'),
        ('Board/Card Game', 'Board/Card Game'),
        ('Other', 'Other'),
    ]
    title = models.CharField(
        max_length=30,
        unique=True,
    )
    category = models.CharField(
        max_length=15,
        choices=GAME_CATEGORIES,
    )
    rating = models.FloatField(
        validators=[MinValueValidator(0.1), MaxValueValidator(5)]
    )
    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1)]
    )
    image_url = models.URLField()
    summary = models.TextField(
        null=True,
        blank=True,
    )

class GameModel(GameBaseModel):
    pass