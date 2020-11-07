from django.urls import path,include
from .views import viewAdminPanel, homView, inscription, InscriptionClient, InscriptionVendeur,activate_account,user_profile,CreerPiece
from .views import DetailsPiece
app_name="app_parts"


urlpatterns = [
    #URL Front
    path('',homView,name="homView"),
    path('Inscription', inscription, name="inscription"),
    path('Inscription/Inscription_client/',InscriptionClient, name="InscriptionClient" ),
    path('Inscription/Inscription_vendeur/', InscriptionVendeur, name="InscriptionVendeur"),
    path('Mon-profile/',user_profile,name="user_profile"),
    path('Details-parts/',DetailsPiece,name="DetailsPiece"),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$' ,activate_account, name='activate'),



    #URL Dashboard
    path('Dashboard',viewAdminPanel,name="viewAdminPanel"),
    path('Dashboard/Creer-piece/',CreerPiece,name="CreerPiece"),
]
