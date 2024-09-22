from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
class FormSignUpWithEmail(UserCreationForm):
    email = forms.EmailField(
        required=True,
        help_text="Required. 254 characters maximum and must be unique."
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("User with this email already exists.")
        return email
