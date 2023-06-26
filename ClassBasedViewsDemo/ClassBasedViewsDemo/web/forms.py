from django import forms

from ClassBasedViewsDemo.web.models import CarModel


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'