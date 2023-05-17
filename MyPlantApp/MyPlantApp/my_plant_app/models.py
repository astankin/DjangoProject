from django.core.validators import MinLengthValidator
from django.db import models

from MyPlantApp.my_plant_app.validators import plant_name_validator

# Create your models here.

TYPES = [
    ('Outdoor Plants', 'Outdoor Plants'),
    ('Indoor Plants', 'Indoor Plants'),
]


class Plant(models.Model):
    plant_type = models.CharField(
        max_length=14,
        choices=TYPES,
    )
    name = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(2), plant_name_validator]
    )
    image = models.URLField()
    description = models.TextField()
    price = models.FloatField()
