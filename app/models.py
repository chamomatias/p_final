from django.db import models

# Modelo para representar los portafolios
class portfolio(models.Model):
    """
    Modelo para gestionar información de portafolios.
    """
    nombre = models.CharField(max_length=50, help_text="Nombre del portafolio (máximo 50 caracteres).")
    descripcion = models.CharField(max_length=100, help_text="Descripción del portafolio (máximo 100 caracteres).")

    def __str__(self):
        """
        Devuelve una representación legible del objeto.
        """
        return f"Nombre: {self.nombre} | Descripción: {self.descripcion}"

# Modelo para gestionar contactos
class contacto(models.Model):
    """
    Modelo para almacenar información de contactos.
    """
    nombre = models.CharField(max_length=50, help_text="Nombre del contacto (máximo 50 caracteres).")
    email = models.EmailField(help_text="Correo electrónico válido del contacto.")
    telefono = models.CharField(max_length=30, help_text="Número de teléfono del contacto (máximo 30 caracteres).")
    mensaje = models.TextField(help_text="Mensaje enviado por el contacto.")

    def __str__(self):
        """
        Devuelve una representación legible del objeto.
        """
        return f"Nombre: {self.nombre} | Email: {self.email} | Teléfono: {self.telefono} | Mensaje: {self.mensaje}"
