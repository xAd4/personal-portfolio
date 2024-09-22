from django.db import models

# Create your models here.

# Summary of life
class Summary(models.Model):
    name = models.CharField(max_length=100, verbose_name="Mi nombre")
    description = models.CharField(max_length=300, verbose_name="Mi descripción")
    address = models.CharField(max_length=100, verbose_name="Mi dirección")
    phone = models.CharField(max_length=15, verbose_name="Mi teléfono celular")
    email = models.EmailField(max_length=100, verbose_name="Mi email")
    created_at = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Resumen"
        verbose_name_plural = "Resumen"

    def __str__(self):
        return 'Resumen de vida CV'
    
# My educational background
class Education(models.Model):
    training = models.CharField(max_length=100, verbose_name="Mi formación")
    timeInvested = models.CharField(max_length=50, verbose_name="Tiempo invertido")
    institute = models.CharField(max_length=100, verbose_name="Instituto o universidad")
    description = models.CharField(max_length=150, verbose_name="Descripción")
    created_at = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Educación"
        verbose_name_plural = "Educación"

    def __str__(self):
        return 'Educación CV'
    
# Experience
class ProffesionalExperience(models.Model):
    job = models.CharField(max_length=100, verbose_name="Trabajo")
    timeWorked = models.CharField(max_length=100, verbose_name="Tiempo trabajado")
    workLocation = models.CharField(max_length=100, verbose_name="Dónde trabajé")
    description = models.CharField(max_length=300, verbose_name="Descripción")
    created_at = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Experiencia profesional"
        verbose_name_plural = "Experiencia profesional"

    def __str__(self):
        return 'Experiencia profesional CV'




