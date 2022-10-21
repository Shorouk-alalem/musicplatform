from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ArtistForm
from artists.models import *
from albums.models import *

def ArtistView(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ArtistForm()
    return render(request, 'ArtistTemplate.html', {'form': form})

def AllArtists(request):
    artists=Artist.objects.all().order_by('id')
    all_artists=[]
    for i in artists:
        artist_albums=i.album_set.all()
        list={
            'id':i.id,
            'stage_name':i.stage_name,
            'social_link':i.social_link_field,
            'albums':artist_albums,
        }
        all_artists.append(list)
    return render(request, 'Atristspage.html',{'all': all_artists})

