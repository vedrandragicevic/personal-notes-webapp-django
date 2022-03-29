from django.forms import ModelForm, widgets
from django import forms
from .models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['note_title', 'note_data', 'priority_type']

        labels = {
            'note_title': 'Note Title',
            'note_data': 'Note Data',
            'priority_type': 'Priority Type'
        }
     

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.fields['note_title'].widget.attrs.update({'class':'form-control'})
        self.fields['note_data'].widget.attrs.update({'class':'form-control'})
        self.fields['priority_type'].widget.attrs.update({'class':'form-control text-center'})
