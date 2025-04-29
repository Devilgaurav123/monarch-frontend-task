# testapp/views.py
from django.shortcuts import render
import os
from django.conf import settings
from .models import Panorama  # Import your model

def panorama_view(request):
    # Get images from the database or static directory
    panoramas = Panorama.objects.all()
    
    if not panoramas.exists():
        # Fallback to static images if no database entries
        image_dir = os.path.join(settings.BASE_DIR, 'testapp/static/images')
        images = []
        if os.path.exists(image_dir):
            images = [
                f'images/{file}' for file in sorted(os.listdir(image_dir))
                if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))
            ][:10]  # Limit to 10 images
        return render(request, 'testapp/index.html', {'images': images})
    
    # If using database images
    images = [panorama.image.url for panorama in panoramas[:10]]
    return render(request, 'testapp/index.html', {'images': images})