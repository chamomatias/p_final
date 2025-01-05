from django.db import models

# Create your models here.
class portfolio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return f"Nombre: {self.nombre} | Descripcion: {self.descripcion}"


class contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=30)
    mensaje = models.TextField()
    def __str__(self):
        return f"Nombre: {self.nombre} | Email: {self.email} | Telefono: {self.telefono} | Mensaje: {self.mensaje}"
