from django import forms
from django.forms import ModelForm, DateInput

from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Piece
from django.contrib.auth.models import User


class SignUpForm_vendeur(UserCreationForm):
    
    organisation = forms.CharField(max_length=100,  label="Renseignez le nom de votre organisation", widget=forms.TextInput(attrs={'type':'text', 'class': 'form-control'}))
    adresse_siege = forms.CharField(max_length=400, label="L'adresse de votre siége social", widget=forms.TextInput(attrs={'type':'text', 'class': 'form-control'}))
    nis = forms.CharField(max_length=100,  label="N° Identification Fiscal", widget=forms.TextInput(attrs={'type':'text', 'class': 'form-control'}))
    nif = forms.CharField(max_length=100,  label="N° Identification Social", widget=forms.TextInput(attrs={'type':'text', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('organisation','adresse_siege','nis','nif', 'username', 'first_name', 'last_name','email')

        widgets= {
            'username' : forms.TextInput(attrs={'type':'text', 'class': 'form-control'}),
            'first_name' : forms.TextInput(attrs={'type':'text', 'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs={'type':'text', 'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'type':'email', 'class': 'form-control'}),
 
           
    
           
        }



class SignUpForm_client(UserCreationForm):
    
   
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

        widgets= {
            'username' : forms.TextInput(attrs={'type':'text', 'class': 'form-control'}),
            'first_name' : forms.TextInput(attrs={'type':'text', 'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs={'type':'text', 'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'type':'email', 'class': 'form-control'}),
           
        }
            
        
