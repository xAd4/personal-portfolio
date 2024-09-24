from django.shortcuts import render
from django.views.generic import DetailView
from .models import Project

# Create your views here.
# Portfolio Detail
class PortfolioDetails(DetailView):
    template_name = "main/portfolio-details.html"
    model = Project
    context_object_name = "proyecto"