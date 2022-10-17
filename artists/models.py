from django.db import models
# Artist Model.
class Artist(models.Model):
    stage_name = models.CharField(max_length=100,  blank=False, unique=True )
    social_link_field = models.URLField( blank=True, null=False)
    #... 5 number of approved albums for each artist 
    def approved_albums(self):
        return self.album_set.all().filter(is_approved=True).count()
    class Meta:
        ordering = ('stage_name',) 
    def __str__(self):
        return self.stage_name
