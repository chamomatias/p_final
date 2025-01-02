from django.urls import path
from app import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('sobre_mi/', views.sobre_mi, name='sobre_mi'),
    path('contacto/', views.contacto, name='contacto'),
]