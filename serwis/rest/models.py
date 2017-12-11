from django.db import models


class Post(models.Model):
    """
    Post Model
    Defines the attributes of a post
    """
    text = models.TextField()
    link = models.TextField()
    date = models.TextField()