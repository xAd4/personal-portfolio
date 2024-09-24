from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

#! Images Config
def custom_upload_to(instance, filename):
    if instance.pk:
        old_instance = Service.objects.get(pk=instance.pk)
        old_instance.image.delete()
    return 'service/' + filename

# Create your models here.

class Service(models.Model):
    icon = models.CharField(max_length=100, verbose_name="Icóno de Bootstrap Icon")
    title = models.CharField(max_length=100, verbose_name="Nombre del servicio")
    description = models.TextField(verbose_name="Descripción del servicio")
    image = models.ImageField(upload_to=custom_upload_to, verbose_name="Imágen descriptiva del servicio")
    created_at = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = ("Servicio")
        verbose_name_plural = ("Servicios")

    def __str__(self):
        return self.title
    
#! Images Config 2
@receiver(post_delete, sender=Service)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)