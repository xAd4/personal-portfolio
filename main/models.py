from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

#! Images Config
def custom_upload_to(instance, filename):
    if instance.pk:
        old_instance = Image.objects.get(pk=instance.pk)
        old_instance.image.delete()
    return 'projects/' + filename

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Categoría de proyecto")
    created_at = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = ("Categoría")
        verbose_name_plural = ("Categorías")

    def __str__(self):
        return self.name
    
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del cliente o compañía")
    created_at = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = ("Cliente")
        verbose_name_plural = ("Clientes")

    def __str__(self):
        return self.name
class Image(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre descriptivo de la imagen")
    image = models.ImageField(upload_to=custom_upload_to, verbose_name="Imagen")
    created_at = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = ("Imagen")
        verbose_name_plural = ("Galería de proyectos")

    def __str__(self):
        return self.name

class Project(models.Model):
    image = models.ImageField(upload_to=custom_upload_to, verbose_name="Imagen descriptiva")
    gallery = models.ManyToManyField(Image, related_name="Proyectos")
    title = models.CharField(max_length=100, verbose_name="Título del proyecto")
    description = models.TextField(verbose_name="Descripción del proyecto")
    testimonial = models.CharField(max_length=500, verbose_name="Testimonios")
    imageTestimonial = models.ImageField(upload_to=custom_upload_to, blank=True, null=True, verbose_name="Persona del testimonio")
    conclusion = models.CharField(max_length=800, verbose_name="Conclusión del proyecto")
    category = models.ManyToManyField(Category, related_name="Categorías", verbose_name="Categoría del proyecto")
    client = models.ManyToManyField(Client, related_name="Clientes", verbose_name="Cliente")
    projectFinished = models.CharField(max_length=100, verbose_name="Fecha de finalización")
    projectUrl = models.URLField(max_length=250, verbose_name="Enlace al proyecto")
    created_at = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = ("Proyecto")
        verbose_name_plural = ("Proyectos")

    def __str__(self):
        return self.title


#! Images Config 2
@receiver(post_delete, sender=Image)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)