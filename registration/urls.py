from django.urls import path
from . import views

urlpatterns = [
 # Otras rutas de tu aplicación
 path("signup/", views.SignUpView.as_view(), name="signup"), # -> URL Sign Up
]