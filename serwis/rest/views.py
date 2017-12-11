from .models import Post
from rest_framework import viewsets
from serwis.rest.serializers import PostSerializer
from django.shortcuts import render


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
