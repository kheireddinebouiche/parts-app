from django import forms


class ContactForm(forms.Form):
    nom = forms.CharField(required=True, label='Votre nom', widget=forms.TextInput(attrs={'type':'text','class':'form-control'}))
    from_email = forms.EmailField(required=True, label='Votre adresse Email',widget=forms.EmailInput(attrs={'type':'email','class':'form-control'}))
    subject = forms.CharField(required=True, label='Le suject de votre message',widget=forms.TextInput(attrs={'type':'text','class':'form-control'}))
    message = forms.CharField(required=True, label='Votre message', widget=forms.Textarea(attrs={'type':'text','class':'form-control'}))
    
    

