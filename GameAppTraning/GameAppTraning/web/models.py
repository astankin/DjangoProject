from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class ProfileModel(models.Model):
    email = models.EmailField()
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(12)],
    )
    password = models.CharField(
        max_length=30,
    )
    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name='First Name'
    )
    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name='Last Name'
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
        verbose_name='Profile Picture'
    )


CATEGORY_CHOICES = {
    ('Action', 'Action'),
    ('Adventure', 'Adventure'),
    ('Puzzle', 'Puzzle'),
    ('Strategy', 'Strategy')
}


class GameModel(models.Model):
    title = models.CharField(
        max_length=30,
        unique=True,
    )
    category = models.CharField(
        max_length=15,
        choices=CATEGORY_CHOICES,
    )
    rating = models.FloatField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0.1), MaxValueValidator(0.5)]
    )
    max_level = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Max Level'
    )
    image_url = models.URLField(
        verbose_name='Image URL'
    )
    summary = models.TextField(
        null=True,
        blank=True,
    )
