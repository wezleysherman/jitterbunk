from django import forms

class BunkForm(forms.Form):
    bunk_name = forms.CharField(label='Bunk user', max_length=200)
