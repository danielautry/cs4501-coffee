from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    email = forms.CharField(label='email', max_length=100)
    cardNumber = forms.CharField(label='cardNumber', max_length=100)
    password = forms.CharField(label='password', max_length=100)
