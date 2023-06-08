from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from Car_Collection_App.profile_app.validators import year_validator


# Create your models here.
class CarModel(models.Model):

    type = models.CharField(
        max_length=10,
        choices=[
            ('Sports Car', 'Sports Car'),
            ('Pickup', 'Pickup'),
            ('Crossover', 'Crossover'),
            ('Minibus', 'Minibus'),
            ('Other', 'Other'),
        ]
    )
    model = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(2)],
    )
    year = models.IntegerField(
        validators=[year_validator],
    )
    image_url = models.URLField(
        verbose_name='Image URL',
    )
    price = models.FloatField(
        validators=[MinValueValidator(1)]
    )