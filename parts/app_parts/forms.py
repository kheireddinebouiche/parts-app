from django import forms
from django.forms import ModelForm, DateInput
#from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Piece
from django.contrib.auth.models import User


class SignUpForm_vendeur(UserCreationForm):
    email = forms.EmailField(max_length=100)
    organisation = forms.CharField(max_length=100,  label="Renseignez le nom de votre organisation")
    adresse_siege = forms.CharField(max_length=400, label="L'adresse de votre siége social")
    nis = forms.CharField(max_length=100,  label="N° Identification Fiscal")
    nif = forms.CharField(max_length=100,  label="N° Identification Social")

    class Meta:
        model = User
        fields = ('organisation','adresse_siege','nis','nif', 'username', 'first_name', 'last_name','email')


class SignUpForm_client(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Required')
   
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

