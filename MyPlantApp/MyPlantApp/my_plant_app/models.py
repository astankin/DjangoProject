from django.core.validators import MinLengthValidator
from django.db import models

from MyPlantApp.my_plant_app.validators import plant_name_validator

# Create your models here.

TYPES = [
    ('Outdoor Plants', 'Outdoor Plants'),
    ('Indoor Plants', 'Indoor Plants'),
]


class PlantModel(models.Model):
    plant_type = models.CharField(
        max_length=14,
        choices=TYPES,
        verbose_name="Type:"
    )
    name = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(2), plant_name_validator],
        verbose_name="Name:"
    )
    image = models.URLField(
        verbose_name="Image Url:"
    )
    description = models.TextField(
        verbose_name="Description:"
    )
    price = models.FloatField(
        verbose_name="Price:"
    )
