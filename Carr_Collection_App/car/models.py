from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from car.validators import year_validator


# Create your models here.
class CarModel(models.Model):
    CAR_TYPES = [
        ('Sports Car', 'Sports Car'),
        ('Pickup', 'Pickup'),
        ('Crossover', 'Crossover'),
        ('Minibus', 'Minibus'),
        ('Other', 'Other'),
    ]
    type = models.CharField(
        max_length=10,
        choices=CAR_TYPES,
    )
    model = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(2)]
    )
    year = models.IntegerField(
        validators=[year_validator]
    )
    image_url = models.URLField()

    price = models.FloatField(
        validators=[MinValueValidator(1)]
    )