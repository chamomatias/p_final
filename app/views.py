from django.shortcuts import  render, redirect
from app.models import contacto
from app.models import portfolio
from app.forms import PortfolioFormulario



# Create your views here.
def inicio(request):
    return render(request, 'app/inicio.html')

def sobre_mi(request):
    return render(request, 'app/sobre_mi.html')

def contacto_view(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        email = request.POST["email"]
        telefono = request.POST["telefono"]
        mensaje = request.POST["mensaje"]

        # Crear un nuevo objeto de contacto y guardarlo en la base de datos
        nuevo_contacto = contacto(nombre=nombre, email=email, telefono=telefono, mensaje=mensaje)
        nuevo_contacto.save()

        return redirect("inicio")  # Redirige a la página de inicio después de guardar
    return render(request, 'app/contacto.html')



def portfolio(request):  # Cambié el nombre para evitar conflicto con el modelo `portfolio`
    return render(request, 'app/portfolio.html')


def form_con_api(request):
    if request.method == "POST":
        mi_formulario = PortfolioFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            curso = Curso(nombre=informacion["curso"], descripcion=informacion["descripcion"])
            curso.save()

            return render(request, "app/inicio.html")
    else:
        mi_formulario = PortfolioFormulario()

    return render(request, "app/form_con_api.html", {"mi_formulario": mi_formulario})