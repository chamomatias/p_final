from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from users.forms import UserRegisterForm

# Vista para manejar el inicio de sesión de usuarios
def login_request(request):
    """
    Maneja el inicio de sesión de usuarios. Valida las credenciales proporcionadas y
    autentica al usuario si son correctas. En caso contrario, muestra un mensaje de error.
    """
    msg_login = ""  # Mensaje de error en caso de credenciales incorrectas
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')  # Obtiene el nombre de usuario del formulario
            contrasenia = form.cleaned_data.get('password')  # Obtiene la contraseña del formulario

            # Autentica al usuario
            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                # Si las credenciales son correctas, inicia sesión y redirige al inicio
                login(request, user)
                return render(request, "app/inicio.html")

        # Si las credenciales son incorrectas, muestra un mensaje de error
        msg_login = "Usuario o contraseña incorrectos"

    # Si el método no es POST, inicializa un formulario vacío
    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})

# Vista para manejar el registro de usuarios
def register(request):
    """
    Maneja el registro de nuevos usuarios. Si el formulario enviado es válido,
    crea un nuevo usuario y lo redirige a la página de inicio.
    """
    msg_register = ""  # Mensaje de error en caso de datos incorrectos
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            # Si los datos del formulario son válidos, guarda un nuevo usuario
            form.save()
            return render(request, "app/inicio.html")

        # Si los datos no son válidos, muestra un mensaje de error
        msg_register = "Error en los datos ingresados"

    # Si el método no es POST, inicializa un formulario vacío
    form = UserRegisterForm()
    return render(request, "users/registro.html", {"form": form, "msg_register": msg_register})
