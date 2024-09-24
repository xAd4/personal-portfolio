from django.contrib import admin
from .models import *
# Register your models here.

# Config Model
class ModelConfig(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")

admin.site.register(Category, ModelConfig)
admin.site.register(Client, ModelConfig)
admin.site.register(Image, ModelConfig)
admin.site.register(Project, ModelConfig)