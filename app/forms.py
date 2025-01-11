from django import forms
from app.models import Portfolio

# Formulario basado en modelo para el modelo "portfolio"
class PortfolioFormulario(forms.ModelForm):
    """
    Formulario para gestionar el modelo 'portfolio' utilizando un formulario basado en modelo.
    """
    class Meta:
        model = Portfolio  # Modelo asociado
        fields = ['nombre', 'descripcion']  # Campos incluidos en el formulario

# Formulario general para buscar cursos
class BuscaCursoForm(forms.Form):
    """
    Formulario genérico para buscar cursos basado en el campo 'nombre'.
    """
    nombre = forms.CharField(
        max_length=100,  # Limite opcional para el tamaño del texto
        required=True,   # El campo es obligatorio
        label="Nombre del curso",  # Etiqueta para el campo
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del curso'})  # Personalización del widget
    )
