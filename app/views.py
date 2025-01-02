from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, 'app/inicio.html')

def portfolio(request):
    return render(request, 'app/portfolio.html')

def sobre_mi(request):
    return render(request, 'app/sobre_mi.html')

def contacto(request):
    return render(request, 'app/contacto.html')