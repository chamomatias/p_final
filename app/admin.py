from django.contrib import admin
from app.models import portfolio,contacto


# Register your models here.
@admin.register(portfolio)
class portfolioAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','descripcion')
    ordering = ('id',)
    search_fields = ('nombre',)
    list_filter = ('nombre',)
    list_editable = ('nombre','descripcion')




@admin.register(contacto)
class contactoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','email','telefono','mensaje')
    ordering = ('id',)
    search_fields = ('nombre',)
    list_filter = ('nombre',)
    list_editable = ('nombre','email','telefono','mensaje')
