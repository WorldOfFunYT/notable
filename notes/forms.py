from django import forms
from django import forms

class NoteForm(forms.Form):
    title = forms.CharField(label='Note Title', max_length=100)
    content = forms.CharField(label='Note Content', max_length=500)