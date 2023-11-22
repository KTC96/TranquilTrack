from django.db import models
from cloudinary.models import CloudinaryField

class SupportLocations(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    slug = models.SlugField(max_length=200, unique=True, blank=False)
    location = models.CharField(max_length=100, blank=False)
    details = models.TextField(blank=True)
    image = CloudinaryField('image', default='placeholder')
    latitude = models.FloatField(max_length=200)
    longitude = models.FloatField(max_length=200)
    contact_number = models.FloatField(max_length=200)
    contact_email = models.FloatField(max_length=200)
