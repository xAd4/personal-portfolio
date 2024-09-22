from django.db import models

# Create your models here.

""" 
Model to store contact messages sent by users through the contact form. 
Fields: 
- name: Name of the user sending the message. 
- email: Contact email to reply to the user. 
- subject: Subject of the message to quickly identify the topic 
- message: Content of the message sent by the user - created_on: Date and time the message was sent.
"""

class ContactMessages(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tu nombre")
    email = models.EmailField(max_length=100, verbose_name="Tu email")
    subject = models.CharField(max_length=100, verbose_name="Asunto")
    message = models.TextField(verbose_name="Contenido")
    created_at = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Mensaje de contacto"
        verbose_name_plural = "Mensajes de contacto"

    def __str__(self):
        return f"{self.name, self.email}"