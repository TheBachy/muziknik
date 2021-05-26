from django.contrib import admin
from django.urls import path

from music import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topten', views.topten, name='topten'),
]
