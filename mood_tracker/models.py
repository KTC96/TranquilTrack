from django.db import models
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class SupportLocations(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    location = models.CharField(max_length=100, blank=False)
    details = models.TextField(blank=True)
    image = CloudinaryField('image', default='placeholder')
    latitude = models.FloatField(max_length=200)
    longitude = models.FloatField(max_length=200)
    contact_number = models.CharField(max_length=200)
    contact_email = models.EmailField(max_length=200)

    
    def __str__(self):
        return self.name

class Achievements(models.Model):
    #creates the model for user achievement tracking
    achievement_id = models.AutoField(primary_key=True, unique=True)
    achievement_name = models.CharField(unique=True, max_length=100)
    achievement_icon = models.ImageField(
                        upload_to='images/', default='../default-pic_ls0v0g.png')
    achievement_description = models.CharField(max_length=250)
    achievement_user = models.ManyToManyField(User, related_name='achievements', blank=True)
    
    def __str__(self):
        return self.achievement_name

class Diary(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, related_name='diaries', blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
        verbose_name_plural = "Diaries"
