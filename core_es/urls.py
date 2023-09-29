from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="inicio"),
    path("contacto/", views.contact, name="contacto"),
    path("servicios/", views.services, name="servicios"),
    path("sobre-nosotros/", views.about, name="sobre-nosotros"),
    path("galeria/", views.gallery, name="galeria"),
    path("template/", views.template, name="template"),
]
