from django.db import models


class Post(models.Model):
    post_title = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    post_text = models.CharField(max_length=600)
    post_image = models.ImageField(upload_to='event_images/')
