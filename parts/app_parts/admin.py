from django.contrib import admin
from .models import Profile,Piece, MarquePiece,FamillePiece, ConstructeurVoiture,Voiture

# Register your models here.

admin.site.register(Piece),
admin.site.register(MarquePiece),
admin.site.register(Voiture),
admin.site.register(FamillePiece),
admin.site.register(ConstructeurVoiture),
admin.site.register(Profile),
