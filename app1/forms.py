from django import forms
from django.core import validators

def validate_Destination(value):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
    if(value[0] not in letters) or (value[1] not in numbers):
        raise forms.ValidationError("Use valid letter/number format, e.g. e2.")

class ChessForm(forms.Form):
    Source=forms.CharField(min_length=2, max_length=2, strip=True,
    widget=forms.TextInput(attrs={'placeholder':'e2','style':'font-size:small'}),
    validators=[validators.MinLengthValidator(1), validators.MaxLengthValidator(2), validate_Destination])
    Destination=forms.CharField(min_length=2, max_length=2, strip=True,
    widget=forms.TextInput(attrs={'placeholder':'e4','style':'font-size:small'}),
    validators=[validators.MinLengthValidator(1), validators.MaxLengthValidator(6), validate_Destination])
