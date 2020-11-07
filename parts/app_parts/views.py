from django.shortcuts import render
from .forms import SignUpForm_vendeur,SignUpForm_client
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage, send_mail, BadHeaderError
from .token_generator import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required




#Partie traitement du frontend
def homView(request):
    return render(request,'FrontPanel/landing-page.html')

def inscription(request):
    return render(request,'FrontPanel/inscription.html')

def InscriptionClient(request):
    form = SignUpForm_client()
    if request.method == 'POST':
        form = SignUpForm_client(request.POST)
        if form.is_valid():
            #permet de ne pas enregistrer l'instance dans la base de donnée
            user = form.save(commit=False)
          


            user.is_active = False
            user.save()

            #permet d'enregistrer le profile de l'utilisateur
            user = form.save()
            user.refresh_from_db()
            
            user.profile.is_client = True
        
            user.save()

            current_site = get_current_site(request)
            email_subject = "Lien d'activation de votre compte entreprise"
            message = render_to_string('FrontPanel/activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
            return render(request, 'FrontPanel/email_sent.html')

    else:    
        context = {
            'form' : form,
        }
        return render(request, 'FrontPanel/inscription-client.html', context)

def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, 'success_activation.html')
    else:
        return HttpResponse('Activation link is invalid!')

def InscriptionVendeur(request):
    form = SignUpForm_vendeur()
    if request.method == 'POST':
        form = SignUpForm_vendeur(request.POST)
        if form.is_valid():
            #permet de ne pas enregistrer l'instance dans la base de donnée
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            #permet d'enregistrer le profile de l'utilisateur
            user = form.save()
            user.refresh_from_db()
            
            user.profile.is_vendeur = True
        
            user.save()

            current_site = get_current_site(request)
            email_subject = "Lien d'activation de votre compte entreprise"
            message = render_to_string('FrontPanel/activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
            return render(request, 'FrontPanel/email_sent.html')

    else:    
        context = {
            'form' : form,
        }
    return render(request, 'FrontPanel/inscription-vendeur.html',context)


@login_required
def user_profile(request):
    return render(request, 'FrontPanel/profile.html')

def DetailsPiece(request):
    return render(request,'FrontPanel/details-piece.html')

#partie traitement du backend
@login_required
def viewAdminPanel(request):
    return render(request, 'AdminPanel/dashboard.html')


@login_required
def CreerPiece(request):
    return render(request,'AdminPanel/creer-piece.html')

@login_required
def OrderPiece(request):
    return render(request,'order-piece.html')



