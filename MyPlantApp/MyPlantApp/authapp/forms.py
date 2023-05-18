from django import forms

from MyPlantApp.authapp.models import ProfileModel


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['username', 'first_name', 'last_name']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['username', 'first_name', 'last_name', 'profile_picture']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
