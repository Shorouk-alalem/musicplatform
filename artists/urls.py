from django.urls import path
from artists.views import ArtistView,AllArtists

urlpatterns = [
    path('create/', ArtistView),
    path('', AllArtists),

]