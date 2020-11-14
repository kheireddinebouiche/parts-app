from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.dispatch import receiver
from django.shortcuts import reverse
from django.utils import timezone
from django.db.models.signals import post_save



MOTORISATION =(
    ('e', 'Essence'),
    ('d', 'Diesel')
)

def increment_profile_id_number():
        dernier_nomber = Profile.objects.all().order_by('id').last()
        if not dernier_nomber:
            return 'user-patrs/' + '1'

        profile_id = dernier_nomber.profile_id
        profile_order_nb = int(profile_id.split('user-parts/')[-1])
        n_profiel_order_nb = profile_order_nb + 1
        n_profile_order_id = 'user-parts/' + str(n_profile_order_nb)
        return n_profile_order_id

class Profile(models.Model):
    profile_id = models.CharField(max_length=1000, default=increment_profile_id_number, null=True, blank=True)
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    organisation = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length= 13,blank=True, null=True)
    adresse = models.CharField(max_length=300,null=True,blank=True)
    photo_de_profile = models.ImageField(null=True, blank=True)
    is_client = models.BooleanField(default=False)
    is_vendeur = models.BooleanField(default=False)
    raison_social = models.CharField(max_length=33,null=True, blank=True)
    adresse_siege = models.CharField(max_length=400, null=True, blank=True)
    nif = models.CharField(max_length=30, null=True, blank=True)
    nis = models.CharField(max_length=30, null=True, blank=True)
    banniere = models.ImageField(null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    note = models.BooleanField(default=False)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nif)
        super(Profile, self).save(*args, **kwargs)


    def __str__(self):
        return self.user.username



class ConstructeurVoiture(models.Model):
    designation = models.CharField(max_length=200, null=True, blank=True)
    banniere = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.designation

class Voiture(models.Model):
    designation = models.CharField(max_length=200, null=True, blank=True)
    annee = models.IntegerField(null=True, blank=True)
    motorisation = models.CharField(max_length=1, choices=MOTORISATION, null=True, blank=True)
    puissance = models.CharField(max_length=10,null=True, blank=True)
    cylindré = models.CharField(max_length=10,null=True, blank=True)
    marque = models.ForeignKey(ConstructeurVoiture, on_delete=models.DO_NOTHING)
    banniere = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.designation

class MarquePiece(models.Model):
    designation = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.designation

class FamillePiece(models.Model):
    designation = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.designation



class Piece(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    num_serie = models.CharField(max_length=100, null=True, blank=True)
    designation = models.CharField(max_length=200, null=True, blank=True)
    prix = models.IntegerField(null=True, blank=True)
    marque = models.ForeignKey(MarquePiece, on_delete=models.CASCADE)
    famille = models.ForeignKey(FamillePiece, on_delete=models.CASCADE)
    voiture = models.ManyToManyField(Voiture)
    banniere = models.ImageField(null=True, blank=True)
    archive = models.BooleanField(default=False, null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.num_serie)
        super(Piece, self).save(*args, **kwargs)
    
    def get_parts_details_client(self):
        return reverse("app_parts:DetailsPiece", kwargs={
            'slug': self.slug
        })

    def get_parts_details_owner(self):
        return reverse("app_parts:DetailsPieceOwner", kwargs={
            'slug': self.slug
        })

    def __str__(self):
        return self.designation



def increment_bon_id_number():
        dernier_nomber = BonReduction.objects.all().order_by('id').last()
        if not dernier_nomber:
            return 'Bon/' + '1'

        id_bon = dernier_nomber.id_bon
        id_bon_nb = int(id_bon.split('Bon/')[-1])
        n_bon_order_nb = id_bon_nb + 1
        n_bon_order_id = 'Bon/' + str(n_bon_order_nb)
        return n_bon_order_id

class BonReduction(models.Model):
    id_bon = models.CharField(max_length=1000, default=increment_bon_id_number, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()
    taux = models.IntegerField(null=True,blank=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.id_bon)
        super(BonReduction, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    











