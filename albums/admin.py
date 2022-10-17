from django.contrib import admin
from albums.models import Album
from artists.models import Artist 
from django import forms
# Register your models here.


#4....txt  help 
class AlbumForm(forms.ModelForm):
    class Meta:
        model=Album
        help_texts={'is_approved':"Approve the album if its name is not explicit"}
        exclude=()

#3... make creation date read only
class AlbumClass(admin.ModelAdmin):
    form=AlbumForm
    model=Album
    def get_readonly_fields(self, request, obj=None):
        if obj:  
            return self.readonly_fields + ('creation_datetime',)
        return self.readonly_fields

#7... Allow admin to create albums for artists 
class InlineAlbum(admin.StackedInline):
    form=AlbumForm
    model=Album
    extra=1
    def get_readonly_fields(self, request, obj=None):
        if obj:  
            return self.readonly_fields + ('creation_datetime',)
        return self.readonly_fields


class ArtistClass(admin.ModelAdmin):
    inlines= [InlineAlbum]
    list_display=('stage_name','approved_albums',)
    

#2.. Add all models 
admin.site.register(Album,AlbumClass)
admin.site.register(Artist,ArtistClass)
