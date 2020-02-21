from django import forms

class CodeForm(forms.Form):
    CHOICES = (('Python 3', 'Python 3'), ("C++", "C++"), ("Rust", "Rust"))
    language = forms.ChoiceField(choices=CHOICES)
    input_code = forms.CharField(widget=forms.Textarea, label="Your code")
