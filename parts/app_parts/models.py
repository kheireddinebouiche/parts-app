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

class Profile(models.Model):
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
    num_serie = models.CharField(max_length=100, null=True, blank=True)
    designation = models.CharField(max_length=200, null=True, blank=True)
    prix = models.IntegerField(null=True, blank=True)
    marque = models.ForeignKey(MarquePiece, on_delete=models.DO_NOTHING)
    famille = models.ForeignKey(FamillePiece, on_delete=models.DO_NOTHING)
    voiture = models.ForeignKey(Voiture, on_delete=models.DO_NOTHING)
    banniere = models.ImageField(null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.num_serie)
        super(Piece, self).save(*args, **kwargs)
    
    def get_parts_details(self):
        return reverse("app_parts:DetailsPiece", kwargs={
            'slug': self.slug
        })

    def __str__(self):
        return self.designation










