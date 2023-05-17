from django.core.validators import MinLengthValidator
from django.db import models

from MyPlantApp.authapp.validators import user_name_validator


# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(2)]
    )
    first_name = models.CharField(
        max_length=20,
        validators=[user_name_validator],
    )
    last_name = models.CharField(
        max_length=20,
        validators=[user_name_validator],
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
