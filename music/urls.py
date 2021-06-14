from django.contrib import admin
from django.urls import path

from music import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topten', views.topten, name='topten'),
    path('song/<int:pk>/', views.SongDetailView.as_view(), name='song_detail'),
    path('song/', views.SongListView.as_view(), name='song_list'),
    path('band/<int:pk>/', views.BandDetailView.as_view(), name='band_detail'),
    path('song/create/', views.SongCreate.as_view(), name='song_create'),
    path('song/<int:pk>/update/', views.SongUpdate.as_view(), name='song_update'),
    path('song/<int:pk>/delete/', views.SongDelete.as_view(), name='song_delete'),

]
