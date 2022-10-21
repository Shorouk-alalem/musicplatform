from django.urls import path
from albums.views import AlbumView

urlpatterns = [
    path('create/', AlbumView),
]