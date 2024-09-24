from django.shortcuts import render
from django.views.generic import DetailView
from .models import Service

# Create your views here.

# Service Detail
class ServiceDetails(DetailView):
    template_name = "services/service-details.html"
    model = Service
    context_object_name = "services"