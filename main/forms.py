from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Code

class CodeForm(forms.Form):
    CHOICES = (('Python 3', 'Python 3'), ("C++", "C++"), ("Rust", "Rust"))
    language = forms.ChoiceField(choices=CHOICES)
    input_code = forms.CharField(widget=forms.Textarea, label="Your code")
