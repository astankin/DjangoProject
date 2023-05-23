from django import forms

from profile.models import ProfileModel


class ProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = ProfileModel
        fields = ['email', 'age', 'password']
