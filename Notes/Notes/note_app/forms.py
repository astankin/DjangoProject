from django import forms

from Notes.note_app.models import NoteModel


class NoteForm(forms.ModelForm):
    class Meta:
        model = NoteModel
        fields = ['tittle', 'content', 'image_url']


class NoteDeleteForm(NoteForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
