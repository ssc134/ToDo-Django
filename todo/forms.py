from django import forms
from todo.models import Note
from datetime import datetime

class NewNoteForm(forms.ModelForm):
    title = forms.CharField(max_length = 150, help_text="Enter Note Title:")
    content = forms.CharField(widget=forms.Textarea, help_text="Enter Note Content:")

    class Meta:
        model = Note
        fields = ('title', 'content')

'''
class EditNoteForm(forms.ModelForm):
    record = Note.objects.get(pk=id)
    title = forms.CharField(max_length=150, default=record.title)
    content = forms.CharField(max_length=150, default=record.content)

    class Meta:
        model = Note
        fields = ('title', 'content')
'''
