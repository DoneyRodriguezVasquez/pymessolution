import datetime
from django.db import models
from django.contrib import admin
from django.utils import timezone


class Contactos(models.Model):
    email = models.EmailField()
    nombre = models.CharField(verbose_name='Nombre', max_length=50)
    telefono = models.CharField(verbose_name='Teléfono', max_length=15)
    mensaje = models.TextField(verbose_name='Mensaje')
    fecha = models.DateTimeField(verbose_name='Fecha', auto_now_add=True)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.email

    

    """
    función que retorna True si se recibió un mensaje de contacto en los últimos 3 días
    se usa el @admin.display decorador para mejorar la apariencia en el sitio de administración
    """
    @admin.display(
        boolean=True,
        ordering='fecha', 
        description='Contacto reciente?'
    )
    def contactos_recientes(self):
        return self.fecha >= timezone.now() - datetime.timedelta(days=3)
