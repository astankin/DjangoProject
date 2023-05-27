from django.core.validators import MinValueValidator
from django.db import models

CHOICES_GENRE = [
    ("Pop Music", "Pop Music"),
    ("Jazz Music", "Jazz Music"),
    ("R&B Music", "R&B Music"),
    ("Rock Music", "Rock Music"),
    ("Country Music", "Country Music"),
    ("Dance Music", "Dance Music"),
    ("Hip Hop Music", "Hip Hop Music"),
    ("Other", "Other"),
]


# Create your models here.
class AlbumModel(models.Model):
    album_name = models.CharField(
        unique=True,
        max_length=30,
        verbose_name='Album Name',
    )
    artist = models.CharField(
        max_length=30,
    )
    genre = models.CharField(
        max_length=30,
        choices=CHOICES_GENRE,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField(
        verbose_name='Image URL'
    )
    price = models.FloatField(
        validators=[MinValueValidator(0)]
    )
