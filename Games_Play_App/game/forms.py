from django import forms

from game.models import GameModel


class GameForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = '__all__'
        labels = {
            'max_level': 'Max Level',
            'image_url': 'Image URL',
        }


class GameDeleteForm(GameForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
