from django.views.generic import TemplateView

# Create your views here.

# Main page
class Home(TemplateView):
    template_name = "core/index.html"

# Portfolio Detail
class PortfolioDetails(TemplateView):
    template_name = "core/portfolio-details.html"

# Service Detail
class ServiceDetails(TemplateView):
    template_name = "core/service-details.html"

# Stater Page
class StaterPage(TemplateView):
    template_name = "core/starter-page.html"
