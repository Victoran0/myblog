from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    image = models.ImageField(upload_to='post_images/', default='victor_codes.png')
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title[0:50]