from django.db import models

# Create your models here.
class Cursos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Contactos(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=30)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre