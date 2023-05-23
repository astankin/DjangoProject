from django import forms

from car.models import CarModel


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'


class CarCreateForm(CarBaseForm):
    pass


class CarDeleteForm(CarBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'


