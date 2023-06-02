from django.db import models


# Create your models here.
class ProfileModel(models.Model):
    first_name = models.CharField(
        max_length=20,
    )
    last_name = models.CharField(
        max_length=20,
    )
    age = models.PositiveIntegerField()
    image_url = models.URLField()

