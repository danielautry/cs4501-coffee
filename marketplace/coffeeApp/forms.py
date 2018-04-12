from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    # email = forms.CharField(label='Email', max_length=100)
    # password = forms.CharField(label='Password', max_length=100)
    # name = forms.CharField(label='Name: ', max_length=100)
