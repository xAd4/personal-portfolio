from django.shortcuts import redirect
from django.views.generic import TemplateView
from contact.forms import ContactMessagesForm
from job.models import *
from services.models import *

# Create your views here.

# Main page
class Home(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs): # -> This logic allows sent instances-model the model DeppartmentAppointment through that form
        context = super().get_context_data(**kwargs)
        context['form'] = ContactMessagesForm()
        context['summary'] = Summary.objects.all()
        context['education'] = Education.objects.all()
        context['experience'] = ProffesionalExperience.objects.all()
        context['services'] = Service.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login') 

        form = ContactMessagesForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('home')
        return self.get(request, *args, **kwargs, form=form)

# Portfolio Detail
class PortfolioDetails(TemplateView):
    template_name = "core/portfolio-details.html"

# Service Detail
class ServiceDetails(TemplateView):
    template_name = "core/service-details.html"

# Stater Page
class StaterPage(TemplateView):
    template_name = "core/starter-page.html"
