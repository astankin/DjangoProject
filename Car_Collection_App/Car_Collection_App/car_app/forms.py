from django import forms

from Car_Collection_App.car_app.models import CarModel


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'


class CarDeleteForm(CarCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
