from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="startseite"),
    path("kontakt/", views.contact, name="kontakt"),
    path("dienstleistungen/", views.services, name="dienstleistungen"),
    path("ueberuns/", views.about, name="ueberuns"),
    path("galerie/", views.gallery, name="galerie"),
    path("template/", views.template, name="template"),
]
