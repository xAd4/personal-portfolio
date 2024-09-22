from django import forms
from .models import ContactMessages

class ContactMessagesForm(forms.ModelForm):
    class Meta:
        model = ContactMessages
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Tu nombre"}),
            "email": forms.TextInput(attrs={"class": "form-control", "placeholder": "Tu email"}),
            "subject": forms.TextInput(attrs={"class": "form-control", "placeholder": "Asunto"}),
            "message": forms.Textarea(attrs={"class": "form-control", "placeholder": "Contenido"}),
        }