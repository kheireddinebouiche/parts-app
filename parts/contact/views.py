from django.shortcuts import render
from .forms import ContactForm

# Create your views here.


def ShowContact(request):
    form = ContactForm()


    context = {
        'form' : form,
    }

    return render(request,'FrontPanel/contact.html', context)