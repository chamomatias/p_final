from django.contrib import admin
from app.models import portfolio, contacto

# Registro del modelo "portfolio" en el administrador de Django
@admin.register(portfolio)
class portfolioAdmin(admin.ModelAdmin):
    """
    Configuración de la interfaz de administración para el modelo 'portfolio'.
    """
    list_display = ('id', 'nombre', 'descripcion')  # Campos mostrados en la lista de objetos
    ordering = ('id',)  # Orden predeterminado por el campo 'id'
    search_fields = ('nombre',)  # Habilita la barra de búsqueda en base al campo 'nombre'
    list_filter = ('nombre',)  # Habilita filtros por el campo 'nombre'
    list_editable = ('nombre', 'descripcion')  # Permite editar los campos directamente en la lista

# Registro del modelo "contacto" en el administrador de Django
@admin.register(contacto)
class contactoAdmin(admin.ModelAdmin):
    """
    Configuración de la interfaz de administración para el modelo 'contacto'.
    """
    list_display = ('id', 'nombre', 'email', 'telefono', 'mensaje')  # Campos mostrados en la lista de objetos
    ordering = ('id',)  # Orden predeterminado por el campo 'id'
    search_fields = ('nombre',)  # Habilita la barra de búsqueda en base al campo 'nombre'
    list_filter = ('nombre',)  # Habilita filtros por el campo 'nombre'
    list_editable = ('nombre', 'email', 'telefono', 'mensaje')  # Permite editar los campos directamente en la lista
