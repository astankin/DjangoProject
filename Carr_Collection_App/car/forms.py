from django import forms

from car.models import CarModel


class CarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'

