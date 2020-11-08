from django.shortcuts import render
from .forms import ContactForm
from .models import Contact
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.


def ShowContact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            
            subject = form.cleaned_data['subject']
            nom = form.cleaned_data['nom']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']

            cntc = Contact(
                email = from_email,
                nom = nom,
                objet = subject,
                message = message,
            )

            cntc.save()
            messages.success(request,'Votre message a été bien envoyer')
            return redirect('contact:ShowContact')

        else:
            messages.warning(request,'Une est survenu')
            return redirect('contact:ShowContact')
            
        
    context = {
        'form' : form,
    }

    return render(request,'FrontPanel/contact.html', context)