from django.shortcuts import  render, redirect
from app.models import contacto
from app.models import portfolio

from app.forms import PortfolioFormulario
from app.forms import BuscaCursoForm



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





def portfolio(request):
    if request.method == "POST":
        form = PortfolioFormulario(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos en la tabla `portfolio`
            return redirect("portfolio")  # Redirige después de guardar
    else:
        form = PortfolioFormulario()

    return render(request, 'app/portfolio.html', {'form': form})



def buscar_form_con_api(request):
    if request.method == "POST":
        mi_formulario = BuscaCursoForm(request.POST) # Aqui me llega la informacion del html

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            nombres = contacto.objects.filter(nombre__icontains=informacion["nombre"])

            return render(request, "app/mostrar_cursos.html", {"nombres": nombres})
    else:
        mi_formulario = BuscaCursoForm()

    return render(request, "app/buscar_form_con_api.html", {"mi_formulario": mi_formulario})
