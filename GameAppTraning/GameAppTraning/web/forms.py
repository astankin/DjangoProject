from django import forms

from GameAppTraning.web.models import GameModel, ProfileModel


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class GameCreateForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = '__all__'
