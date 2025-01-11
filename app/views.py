from django.shortcuts import render, redirect
from app.models import Contacto, Portfolio
from app.forms import PortfolioFormulario, BuscaCursoForm
from django.http import HttpResponseRedirect



# Vista para la página de inicio
def inicio(request):
    """
    Renderiza la página de inicio.
    """
    return render(request, 'app/inicio.html')

# Vista para la página "Sobre mí"
def sobre_mi(request):
    """
    Renderiza la página 'Sobre mí'.
    """
    return render(request, 'app/sobre_mi.html')

# Vista para la página "Sobre nosotros"
def sobre_nosotros(request):
    """
    Renderiza la página 'Sobre nosotros'.
    """
    return render(request, 'app/sobre_nosotros.html')


# Vista para manejar el formulario de contacto
def contacto_view(request):
    """
    Maneja el formulario de contacto. Si se envía un formulario válido, guarda los datos
    en la base de datos y redirige a la página de inicio.
    """
    if request.method == "POST":
        nombre = request.POST["nombre"]
        email = request.POST["email"]
        telefono = request.POST["telefono"]
        mensaje = request.POST["mensaje"]

        # Crear y guardar un nuevo objeto de contacto
        nuevo_contacto = contacto(nombre=nombre, email=email, telefono=telefono, mensaje=mensaje)
        nuevo_contacto.save()

        # Redirige a la página de inicio después de guardar
        return redirect("inicio")
    
    # Renderiza la página de contacto si el método no es POST
    return render(request, 'app/contacto.html')

# Vista para manejar el portafolio
def portfolio(request):
    """
    Maneja el formulario del portafolio. Si se envía un formulario válido, guarda los datos
    en la tabla `portfolio` y redirige a la misma página.
    """
    if request.method == "POST":
        form = PortfolioFormulario(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos en la base de datos
            return redirect("portfolio")  # Redirige después de guardar
    else:
        form = PortfolioFormulario()  # Inicializa un formulario vacío

    # Renderiza la página del portafolio
    return render(request, 'app/portfolio.html', {'form': form})




def registrar_contacto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        telefono = request.POST.get("telefono")
        mensaje = request.POST.get("mensaje")

        # Guarda los datos en la base de datos
        nuevo_contacto = Contacto(
            nombre=nombre,
            email=email,
            telefono=telefono,
            mensaje=mensaje,
        )
        nuevo_contacto.save()

        # Redirige a una página de éxito (o al mismo formulario)
        return HttpResponseRedirect('/gracias/')  # Ajusta la URL según sea necesario

    return render(request, 'app/inicio.html')

def gracias(request):
    return render(request, 'app/gracias.html')



# Vista para buscar cursos mediante un formulario
def buscar_form_con_api(request):
    """
    Maneja un formulario para buscar contactos por nombre. Filtra los contactos en la base
    de datos y los muestra en una página.
    """
    if request.method == "POST":
        mi_formulario = BuscaCursoForm(request.POST)  # Procesa el formulario enviado
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data  # Obtiene los datos limpiados del formulario
            
            # Filtra los contactos cuyos nombres contengan el texto ingresado
            nombres = contacto.objects.filter(nombre__icontains=informacion["nombre"])

            # Renderiza los resultados en la plantilla
            return render(request, "app/mostrar_cursos.html", {"nombres": nombres})
    else:
        mi_formulario = BuscaCursoForm()  # Inicializa un formulario vacío

    # Renderiza la página de búsqueda con el formulario
    return render(request, "app/buscar_form_con_api.html", {"mi_formulario": mi_formulario})
