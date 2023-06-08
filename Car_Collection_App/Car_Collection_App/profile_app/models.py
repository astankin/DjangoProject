from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from Car_Collection_App.profile_app.validators import year_validator


# Create your models here.
class ProfileModel(models.Model):
    username = models.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(2, 'The username must be a minimum of 2 chars'),
        ]
    )
    email = models.EmailField()
    age = models.IntegerField(
        validators=[MinValueValidator(18)],
    )
    password = models.CharField(
        max_length=30,
    )
    first_name = models.CharField(
        verbose_name='First Name',
        max_length=30,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=30,
        null=True,
        blank=True,
    )
    profile_picture = models.URLField(
        verbose_name='Profile Picture',
        null=True,
        blank=True,
    )