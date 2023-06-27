from django.db import models
from django.urls import reverse


# Create your models here.
class CarModel(models.Model):
    model = models.CharField(
        max_length=20,

    )
    type = models.CharField(
        max_length=20,

    )
    year_of_manufacturing = models.PositiveIntegerField()
    #Adding Absolute url where to redirect after success
    #can be added in Module or in the View `success_url = reverse_lazy('dashboard')`
    # def get_absolute_url(self):
    #     return reverse('dashboard')
    #     return reverse('details-car', kwargs={'pk': self.pk}) # if we want to redirect to details-car
