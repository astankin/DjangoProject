from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from Exam_Preparation.profile_app.validators import username_validator


# Create your models here.
class ProfileModel(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            username_validator
        ]
    )
    email = models.EmailField()
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0)]
    )
