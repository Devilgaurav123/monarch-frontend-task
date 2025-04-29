# testapp/models.py
from django.db import models

class Panorama(models.Model):
    # Define your model fields here
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='panoramas/')

    def __str__(self):
        return self.name
