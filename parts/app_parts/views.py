from django.shortcuts import render
from .forms import SignUpForm_vendeur,SignUpForm_client, ProfileFormVendeur,ProfileFormClient, UserForm,CreerPieceForm
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
from django.db import transaction
from django.shortcuts import redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .models import Piece, Voiture
from django.shortcuts import get_object_or_404



#Partie traitement du frontend
def homView(request):
    return render(request,'FrontPanel/landing-page.html')

def inscription(request):
    return render(request,'FrontPanel/inscription.html')

@transaction.atomic
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
            user.profile.adresse = form.cleaned_data.get('adresse')
            user.profile.phone_number = form.cleaned_data.get('phone_number')
            user.profile.is_client = True
        
            user.save()

            #Envoie d'un email d'activation de compte
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
            messages.warning(request,'Une erreur est survenu, veuillez réessayer')
            return redirect('app_parts:InscriptionClient')

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

@login_required
@transaction.atomic
@csrf_protect
def update_profile_vendeur(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileFormVendeur(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Votre profile a été mit a jour avec succées'))
            return redirect('app_parts:update_profile_vendeur')
        else:
            messages.error(request, 'Corriger les erreurs')
            return redirect('app_parts:update_profile_vendeur')

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileFormVendeur(instance=request.user.profile)
    return render(request, 'FrontPanel/update-profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
@transaction.atomic
@csrf_protect
def update_profile_client(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileFormClient(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Votre profile a été mit a jour avec succées'))
            return redirect('app_parts:update_profile_client')
        else:
            messages.error(request, 'Please correct the error below')

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileFormClient(instance=request.user.profile)
    return render(request, 'FrontPanel/update-profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@transaction.atomic
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
            user.profile.organisation = form.cleaned_data.get('organisation')
            user.profile.adresse_siege = form.cleaned_data.get('adresse_siege')
            user.profile.phone_number = form.cleaned_data.get('phone_number')
            user.profile.nis =  form.cleaned_data.get('nis')
            user.profile.is_vendeur = True
        
            user.save()

            #Envoie d'un email d'activation de compte
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

def ShowCatalogue(request):
    return render(request,'FrontPanel/catalogue.html')


def ShowTerms(request):
    return render(request,'FrontPanel/terms.html')

def AboutUs(request):
    return render(request,'FrontPanel/about-us.html')


@login_required
def user_profile(request):
    return render(request, 'FrontPanel/profile.html')

def DetailsPiece(request, slug):
    obj = get_object_or_404(Piece, slug=slug)

    context = {
        'obj' : obj,
    }

    return render(request,'FrontPanel/details-piece.html', context)

##########################################################
##############partie traitement du backend################
##########################################################
@login_required
def viewAdminPanel(request):
    return render(request, 'AdminPanel/dashboard.html')


@login_required
def ViewPieceControl(request):
    piece = Piece.objects.filter(user=request.user)

    context = {
        'piece' : piece,
    }
    return render(request,'AdminPanel/controle-piece.html', context)


@login_required
def CreerPiece(request):
    form = CreerPieceForm()
    if request.method == "POST":
        form = CreerPieceForm(request.POST)
        if form.is_valid():
            num_serie = form.cleaned_data.get('num_serie')
            designation = form.cleaned_data.get('designation')
            marque = form.cleaned_data.get('marque')
            famille = form.cleaned_data.get('famille')
            prix = form.cleaned_data.get('prix')
            voiture = form.cleaned_data.get('voiture')

            info = form.save(commit=False)
            info = Piece(
                user = request.user,
                num_serie= num_serie,
                marque = marque,
                famille = famille,
                designation = designation,
                prix = prix,
               
            )     
            info.save()

            selected_voiture = form.cleaned_data.get('voiture') #returns list of all selected categories e.g. ['Sports','Adventure']
            #Now saving the ManyToManyField, can only work after saving the form
            for title in selected_voiture:
                voiture_obj = Voiture.objects.get(designation=title) #get object by title i.e I declared unique for title under Category model
                info.voiture.add(voiture_obj) #now add each category object to the saved form object
            
            messages.success(request,'Votre article a été enregistrer avec succes')
            return redirect('app_parts:CreerPiece')
        else:
            messages.warning(request,'Une erreur est survenu, veuillez réessayer')
            return redirect('app_parts:CreerPiece')


    context = {
        'form' : form
    }
    return render(request,'AdminPanel/creer-piece.html', context)

@login_required
def DetailsPieceOwner(request, slug):
    obj = get_object_or_404(Piece, slug=slug)

    context = {
        'obj' : obj
    }
   

    return render(request,'AdminPanel/Details-piece-admin.html', context)

@login_required
def OrderPiece(request):
    return render(request,'order-piece.html')

@login_required
def Commandes(request):
    if request.user.profile.is_vendeur or request.user.is_staff:
        return render(request, 'AdminPanel/commandes-admin.html')
    else:
        return HttpResponse("Vous n'etes pas autoriser a consulter cette page")


@login_required
def BonReductionView(request):
    if request.user.profile.is_vendeur or request.user.is_staff:
        return render(request, 'AdminPanel/bon-reduction.html')
    else:
        return HttpResponse("Vous n'etes pas autoriser a consulter cette page")


@login_required
def ArchiveAdminView(request):
    if request.user.profile.is_vendeur or request.user.is_staff:
        return render(request, 'AdminPanel/archive-admin.html')
    else:
        return HttpResponse("Vous n'etes pas autoriser a consulter cette page")


@login_required
def StockAdminView(request):
    if request.user.profile.is_vendeur or request.user.is_staff:
        return render(request, 'AdminPanel/stock-admin.html')
    else:
        return HttpResponse("Vous n'etes pas autoriser a consulter cette page")

@login_required
def Assistance(request):
    if request.user.profile.is_vendeur or request.user.is_staff:
        return render(request,'AdminPanel/assistance-admin.html')
    else:
        return HttpResponse("Vous n'etes pas autoriser a consulter cette page")

@login_required
def Aide(request):
    if request.user.profile.is_vendeur or request.user.is_staff:
        return render(request,'AdminPanel/aide-admin.html')
    else:
        return HttpResponse("Vous n'etes pas autoriser a consulter cette page")




