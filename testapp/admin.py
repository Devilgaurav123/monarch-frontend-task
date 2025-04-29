# testapp/admin.py
from django.contrib import admin
from .models import Panorama

@admin.register(Panorama)
class PanoramaAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image']  # Customize as needed


