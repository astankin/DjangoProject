from django.db import models


# Create your models here.
class CarModel(models.Model):
    model = models.CharField(
        max_length=20,

    )
    type = models.CharField(
        max_length=20,

    )
    year_of_manufacturing = models.PositiveIntegerField()
