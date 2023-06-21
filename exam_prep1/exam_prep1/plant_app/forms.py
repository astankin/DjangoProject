from django import forms

from exam_prep1.plant_app.models import PlantModel


class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = PlantModel
        fields = '__all__'


class PlantCreateForm(PlantBaseForm):
    pass


class PlantDeleteForm(PlantBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
