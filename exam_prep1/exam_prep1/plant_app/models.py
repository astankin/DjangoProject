from django.core.validators import MinLengthValidator
from django.db import models

from exam_prep1.plant_app.validators import plant_name_validator

TYPE_CHOICES = [
    ("Outdoor Plants", "Outdoor Plants"),
    ("Indoor Plants", "Indoor Plants"),
]


# Create your models here.
class PlantModel(models.Model):
    type = models.CharField(
        max_length=14,
        choices=TYPE_CHOICES,
    )
    name = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(2),
            plant_name_validator],
    )
    image_url = models.URLField(
        verbose_name='Image URL'
    )
    description = models.TextField()
    price = models.FloatField(
        verbose_name="Price:"
    )
