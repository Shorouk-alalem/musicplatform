from django.forms import ModelForm,forms
from albums.models import Album
from django.forms import SelectDateWidget

class AlbumForm(ModelForm):

    class Meta:
        model = Album
        fields = ['name', 'artist_name', 'release_datetime', 'cost']
        #widgets = {
        #    'release_datetime':  SelectDateWidget(),
        #}
