from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError


def validar_telefono(value):
    if not value.replace("+", "").replace(" ", "").isdigit():
        raise ValidationError("El número de teléfono solo puede contener dígitos, espacios y '+'.")


class Portfolio(models.Model):
    """
    Modelo para gestionar información de portafolios.
    """
    nombre = models.CharField(max_length=50, help_text="Nombre del portafolio (máximo 50 caracteres).")
    descripcion = models.CharField(max_length=100, help_text="Descripción del portafolio (máximo 100 caracteres).")

    class Meta:
        verbose_name = "Portafolio"
        verbose_name_plural = "Portafolios"

    def __str__(self):
        return f"Nombre: {self.nombre} | Descripción: {self.descripcion}"


class Contacto(models.Model):
    """
    Modelo para almacenar información de contactos.
    """
    nombre = models.CharField(max_length=50, help_text="Nombre del contacto (máximo 50 caracteres).")
    email = models.EmailField(help_text="Correo electrónico válido del contacto.")
    telefono = models.CharField(
        max_length=30,
        validators=[validar_telefono],
        help_text="Número de teléfono del contacto (máximo 30 caracteres)."
    )
    mensaje = models.TextField(help_text="Mensaje enviado por el contacto.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora de creación del registro.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Fecha y hora de la última actualización.")

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"

    def __str__(self):
        return f"{self.nombre} ({self.email})"
