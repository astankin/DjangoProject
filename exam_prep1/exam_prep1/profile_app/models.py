from django.core.validators import MinLengthValidator
from django.db import models

from exam_prep1.profile_app.validators import profile_name_validator


# Create your models here.
class ProfileModel(models.Model):
    username = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(2)],
    )
    first_name = models.CharField(
        max_length=20,
        validators=[profile_name_validator],
        verbose_name='First Name',
    )
    last_name = models.CharField(
        max_length=20,
        validators=[profile_name_validator],
        verbose_name='Last Name',
    )
    profile_picture = models.URLField(
        blank=True,
        null=True,
        verbose_name='Profile Picture'
    )

