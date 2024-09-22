from django.contrib import admin
from .models import Summary, Education, ProffesionalExperience

# Register your models here.

# Config Model
class ModelConfig(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

admin.site.register(Summary, ModelConfig)
admin.site.register(Education, ModelConfig)
admin.site.register(ProffesionalExperience, ModelConfig)