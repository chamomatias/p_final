from django.urls import path
from app import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('Cursos/', views.Cursos, name='Cursos'),
    path('acerca_de_mi/', views.acerca_de_mi, name='acerca_de_mi'),
    path('Contactos/', views.Contactos, name='Contactos'),
]