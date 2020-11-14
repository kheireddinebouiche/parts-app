from django.urls import path,include
from .views import viewAdminPanel, homView, inscription, InscriptionClient, InscriptionVendeur,activate_account,user_profile,CreerPiece
from .views import DetailsPiece,ShowCatalogue,AboutUs,update_profile_vendeur,update_profile_client,ViewPieceControl,DetailsPieceOwner
from .views import Commandes,BonReductionView,ArchiveAdminView,StockAdminView,Aide,Assistance

app_name="app_parts"


urlpatterns = [
    #URL Front
    path('',homView,name="homView"),
    path('Inscription', inscription, name="inscription"),
    path('Inscription/Inscription_client/',InscriptionClient, name="InscriptionClient" ),
    path('Inscription/Inscription_vendeur/', InscriptionVendeur, name="InscriptionVendeur"),
    path('Mon-profile/',user_profile,name="user_profile"),
    path('Mon-profile/update_profile_vendeur',update_profile_vendeur,name="update_profile_vendeur"),
    path('Mon-profile/update_profile_client',update_profile_client,name="update_profile_client"),
    path('Details-parts/<slug>/',DetailsPiece,name="DetailsPiece"),
    path('Notre-catalogue/',ShowCatalogue,name="ShowCatalogue"),
    path('About-us/',AboutUs,name="AboutUs"),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$' ,activate_account, name='activate'),



    #URL Dashboard
    path('Dashboard',viewAdminPanel,name="viewAdminPanel"),
    path('Dashboard/parts/',ViewPieceControl,name="ViewPieceControl"),
    path('Dashboard/Creer-piece/',CreerPiece,name="CreerPiece"),
    path('Dashboard/Details-piece-user/<slug>/',DetailsPieceOwner,name="DetailsPieceOwner"),

    path('Dashboard/Commandes/',Commandes,name="Commandes"),
    path('Dashboard/Bon-reduction/',BonReductionView,name="BonReductionView"),
    path('Dashboard/Archive-admin/',ArchiveAdminView,name="ArchiveAdminView"),
    path('Dashboard/Stock-article-admin/',StockAdminView,name="StockAdminView"),

    path('Dashboard/Assistance/',Assistance,name="Assistance"),
    path('Dashboard/Aide/',Aide,name="Aide"),
]
