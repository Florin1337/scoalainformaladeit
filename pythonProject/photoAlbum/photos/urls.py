from django.urls import path
from . import views

#gallery este pagina principala ( homepage )
#photo deschide o pagina noua cu id-ul fiecarei imagini si o afiseaza impreuna cu descrierea ei si un buton de back spre homepage
#add adauga functionalitatea de a adauga poze noi

urlpatterns = [
    path("", views.gallery, name="gallery"),
    path("photo/<str:pk>/", views.viewPhoto, name="photo"),
    path("add/", views.addPhoto, name="add"),
]