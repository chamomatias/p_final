from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Formulario para registrar nuevos usuarios
class UserRegisterForm(UserCreationForm):
    """
    Formulario personalizado para registrar nuevos usuarios. Incluye los campos de
    email, contraseña y confirmación de contraseña, además de los predeterminados.
    """
    email = forms.EmailField(
        required=True,  # El campo email es obligatorio
        label="Correo electrónico",  # Etiqueta para el campo
        help_text="Ingrese una dirección de correo válida."  # Texto de ayuda
    )
    password1 = forms.CharField(
        label='Contraseña',  # Etiqueta para la contraseña
        widget=forms.PasswordInput,  # Widget para ocultar el texto
        help_text="La contraseña debe contener al menos 8 caracteres y no puede ser común."
    )
    password2 = forms.CharField(
        label='Repetir contraseña',  # Etiqueta para confirmar la contraseña
        widget=forms.PasswordInput,  # Widget para ocultar el texto
        help_text="Ingrese la misma contraseña para confirmarla."
    )

    class Meta:
        """
        Configuración del formulario:
        - Asociado al modelo `User`.
        - Incluye campos específicos: username, email, password1, password2.
        - Elimina los mensajes de ayuda predeterminados.
        """
        model = User
        fields = ["username", "email", "password1", "password2"]  # Campos incluidos en el formulario
        help_texts = {k: "" for k in fields}  # Elimina los textos de ayuda predeterminados
