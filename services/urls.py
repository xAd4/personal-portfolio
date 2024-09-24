from django.urls import path
from . import views

urlpatterns = [
    path("service/<int:pk>/", views.ServiceDetails.as_view(), name="service-details"),
]
