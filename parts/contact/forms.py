from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, label='Votre adresse Email')
    subject = forms.CharField(required=True, label='Le suject de votre message')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Votre message')

