from django.db import models

# Create your models here.

class Service(models.Model):
    icon = models.CharField(max_length=100, verbose_name="Icóno de Bootstrap Icon")
    title = models.CharField(max_length=100, verbose_name="Nombre del servicio")
    description = models.TextField(verbose_name="Descripción del servicio")
    created_at = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = ("Servicio")
        verbose_name_plural = ("Servicios")

    def __str__(self):
        return self.title