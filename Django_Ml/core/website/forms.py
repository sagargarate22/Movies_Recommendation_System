from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    username = forms.CharField(label="",max_length=10,required=True,
                               widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}))
    password1 = forms.CharField(label="",max_length=10,required=True,
                                widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Password','type':'password'}))
    password2 = forms.CharField(label="",max_length=10,required=True,
                                widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Conform Password','type':'password'}))
    
    class meta:
        model = User
        fields = ('username','password1','password2')