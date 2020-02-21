from django import forms

class CodeForm(forms.Form):
    input_code = forms.CharField(widget=forms.Textarea, label="Your code")