from cloudinary.models import CloudinaryField
from django.db import models


# Create your models here.
class Photo(models.Model):
    image = CloudinaryField('image')
