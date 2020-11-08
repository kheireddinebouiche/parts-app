from django.urls import path,include
from .views import ShowContact
app_name="contact"


urlpatterns = [
    #URL Front
    path('Contact-us',ShowContact, name="ShowContact"),
]
