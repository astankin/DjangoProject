from django import forms

from profile.models import ProfileModel


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                }),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                }),
            'age': forms.NumberInput(
                attrs={
                    'placeholder': 'Age',
                }),
        }
