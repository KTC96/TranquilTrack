from django.db import models

# Create your models here.
class Achievements(models.Model):
    #creates the model for user achivement tracking
    achievement_id = models.AutoField(primary_key=True, unique=True)
    achievement_name = models.CharField(unique=True, max_length=100)
    achievement_icon = models.ImageField(
                        upload_to='images/', default='../default-pic_ls0v0g.png')
    achievement_description = models.CharField(max_length=250)