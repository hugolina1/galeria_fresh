from django.db import models


class Post(models.Model):
    """
    Post Model
    Defines the attributes of a post
    """
#    id = models.IntegerField(primary_key=True)
    text = models.TextField()
#    link = models.TextField()
#    date = models.TextField()