from django.urls import path
from . import views


app_name = "root"
urlpatterns = [
    path("", views.index, name="index"),
    path("PET-4/", views.pet4, name="pet4"),
    path("GLASS-6/", views.glass6, name="glass6"),
    path("CAN-1/", views.can1, name="can1"),
    path("PET-2/", views.pet2, name="pet2"),
    path("PET-KEG/", views.petkeg, name="petkeg"),
    path("KEG/", views.keg, name="keg"),
    path("help/", views.help, name="help"),
    path("contacts/", views.contacts, name="contacts"),
    path("review/", views.review, name="review"),
    ]
