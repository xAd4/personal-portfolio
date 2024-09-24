from django.urls import path
from . import views

urlpatterns = [
    path("portfolio/<int:pk>/", views.PortfolioDetails.as_view(), name="portfolio-details"),
]
