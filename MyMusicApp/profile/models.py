from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from profile.validators import name_validator


# Create your models here.


class ProfileModel(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            name_validator,
        ]
    )
    email = models.EmailField()

    age = models.IntegerField(
        validators=[
            MinValueValidator(0)
        ],
        null=True,
        blank=True,

    )
