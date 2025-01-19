from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(label='username', max_length=30)
    password = forms.CharField(label='password', widget=forms.PasswordInput, min_length=8)
    repeat_password = forms.CharField(label='repeat_password', widget=forms.PasswordInput, min_length=8)
    age = forms.CharField(label='age', widget=forms.NumberInput, min_value=18, max_value=100)
