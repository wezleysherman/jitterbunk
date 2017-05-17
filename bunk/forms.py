from django import forms

class BunkForm(forms.Form):
    bunk_name = forms.CharField(label='Bunk user', max_length=200)

# TO-DO: Need to make charfield private for password
class LoginForm(forms.Form):
    user_name = forms.CharField(label='User name', max_length=200)
    user_pass = forms.CharField(label='Password', max_length=200, widget=forms.PasswordInput())
