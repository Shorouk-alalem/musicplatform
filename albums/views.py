from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import AlbumForm

def AlbumView(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AlbumForm()
    return render(request, 'AlbumTemplate.html', {'form': form})
