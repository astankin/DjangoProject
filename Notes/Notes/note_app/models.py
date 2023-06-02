from django.db import models


# Create your models here.
class NoteModel(models.Model):
    tittle = models.CharField(
        max_length=30,
    )
    image_url = models.URLField(
        verbose_name='Link to image'
    )
    content = models.TextField()
