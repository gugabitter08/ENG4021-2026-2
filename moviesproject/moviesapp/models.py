from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_lenght = 200)
    description = models.TextField()
    image_url = models.URLField(max_lenght = 500)