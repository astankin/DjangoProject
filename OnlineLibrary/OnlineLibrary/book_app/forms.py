from django import forms

from OnlineLibrary.book_app.models import BookModel


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
            'image': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'type': forms.TextInput(attrs={'placeholder': 'Fiction, Novel, Crime....'}),
        }