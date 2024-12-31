from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, 'app/inicio.html')

def Cursos(request):
    return render(request, 'app/Cursos.html')

def acerca_de_mi(request):
    return render(request, 'app/acerca_de_mi.html')

def Contactos(request):
    return render(request, 'app/Contactos.html')