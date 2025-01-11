from django.contrib import admin
from app.models import Portfolio, Contacto

# Registro del modelo "Portfolio" en el administrador de Django
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    """
    Configuración de la interfaz de administración para el modelo 'Portfolio'.
    """
    list_display = ('id', 'nombre', 'descripcion')  # Campos mostrados en la lista de objetos
    ordering = ('id',)  # Orden predeterminado por el campo 'id'
    search_fields = ('nombre',)  # Habilita la barra de búsqueda en base al campo 'nombre'
    list_filter = ('nombre',)  # Habilita filtros por el campo 'nombre'
    list_editable = ('nombre', 'descripcion')  # Permite editar los campos directamente en la lista

# Registro del modelo "Contacto" en el administrador de Django
@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    """
    Configuración de la interfaz de administración para el modelo 'Contacto'.
    """
    list_display = ('id', 'nombre', 'email', 'telefono', 'mensaje')  # Campos mostrados en la lista de objetos
    ordering = ('id',)  # Orden predeterminado por el campo 'id'
    search_fields = ('nombre',)  # Habilita la barra de búsqueda en base al campo 'nombre'
    list_filter = ('nombre',)  # Habilita filtros por el campo 'nombre'
    list_editable = ('nombre', 'email', 'telefono', 'mensaje')  # Permite editar los campos directamente en la lista
