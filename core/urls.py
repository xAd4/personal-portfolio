from django.urls import path
from . import views

# Core URLs
urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("portfolio/", views.PortfolioDetails.as_view(), name="portfolio-details"),
    path("stater/page/", views.StaterPage.as_view(), name="stater-page"),
]
