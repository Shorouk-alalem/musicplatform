from django.forms import ModelForm
from artists.models import Artist

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'