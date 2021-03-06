from django import forms
from django.forms import ModelForm, DateInput

from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Piece
from django.contrib.auth.models import User



class SignUpForm_vendeur(UserCreationForm):
    organisation = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'type':'text','class':'form-control'}))
    adresse_siege = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'type':'text','class':'form-control'}))
    phone_number = forms.CharField(required=True, max_length=14, widget=forms.TextInput(attrs={'type':'text','class':'form-control'}))
    nif = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={'type':'text','class':'form-control'}))
    nis = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={'type':'text','class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email','organisation','adresse_siege','phone_number','nis','nif')
        widgets= {
            'username' : forms.TextInput(attrs={'type':'text', 'class': 'form-control'}),
            'first_name' : forms.TextInput(attrs={'type':'text', 'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs={'type':'text', 'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'type':'email', 'class': 'form-control'}),
            
        } 


class SignUpForm_client(UserCreationForm):
    adresse = forms.CharField(required=True, max_length=100,widget=forms.TextInput(attrs={'type':'text', 'class': 'form-control'}))
    phone_number = forms.CharField(required=True, max_length=14,widget=forms.TextInput(attrs={'type':'text', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','adresse','phone_number', 'email')
        widgets= {
            'username' : forms.TextInput(attrs={'type':'text', 'class': 'form-control'}),
            'first_name' : forms.TextInput(attrs={'type':'text', 'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs={'type':'text', 'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'type':'email', 'class': 'form-control'}),
           
        }
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name' : forms.TextInput(attrs={'type':'text','class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'type':'text','class':'form-control'}),
            'email' : forms.EmailInput(attrs={'type':'text','class':'form-control'}),
        }

class ProfileFormVendeur(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('organisation', 'phone_number','adresse_siege','nif','nis')
        widgets = {
            'organisation' : forms.TextInput(attrs={'type':'text','class':'form-control','placeholder':'Le nom de votre entreprise'}),
            'phone_number' : forms.TextInput(attrs={'type':'text','class':'form-control','placeholder':'N° de téléphone'}),
            'adresse_siege' : forms.TextInput(attrs={'type':'text','class':'form-control'}),
            'nif' : forms.TextInput(attrs={'type':'text','class':'form-control','placeholder':'N° identification fiscal'}),
            'nis' : forms.TextInput(attrs={'type':'text','class':'form-control','placeholder':'N° identification social'}),

        }

class ProfileFormClient(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_number','adresse')
        widgets = {
            'phone_number' : forms.TextInput(attrs={'type':'text','class':'form-control','placeholder':'N° de téléphone'}),
            'adresse' : forms.TextInput(attrs={'type':'text','class':'form-control'}),
        
        }


class CreerPieceForm(forms.ModelForm):
    class Meta:
        model = Piece
        fields = ('num_serie','designation','prix','marque','famille','voiture')
        widgets = {
            'num_serie' : forms.TextInput(attrs={'type':'text','class':'form-control'}),
            'designation' : forms.TextInput(attrs={'type':'text','class':'form-control'}),
            'prix' : forms.TextInput(attrs={'type':'text','class':'form-control'}),
            'marque' : forms.Select(attrs={'type':'text','class':'form-control'}),
            'famille' : forms.Select(attrs={'type':'text','class':'form-control'}),
            'voiture' : forms.SelectMultiple(attrs={'type':'text','class':'form-control'}),
        }
