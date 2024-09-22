from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

# Core URLs
urlpatterns = [
    path("", login_required(views.Home.as_view()), name="home"),
    path("portfolio/", views.PortfolioDetails.as_view(), name="portfolio-details"),
    path("service/", views.ServiceDetails.as_view(), name="service-details"),
    path("stater/page/", views.StaterPage.as_view(), name="stater-page"),
]
