"""rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD:rest/rest/urls.py
from django.conf.urls import url
from rest.api.views import PostListCreateAPIView
=======
from django.conf.urls import url, include
from rest_framework import routers
from rest import views
>>>>>>> a6c0765b6801b8caee53e5efc11f0f1b468bf419:serwis/serwis/urls.py


urlpatterns = [
    url(
        regex=r'^api/$',
        view=PostListCreateAPIView.as_view(),
        name='post_rest_api'
    )
]
