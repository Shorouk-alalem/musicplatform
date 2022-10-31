from email.policy import default
from django.db import models
from artists.models import Artist 
import datetime
from django.utils import timezone
# albums Model.
#Task3: 1- Instead of having an explicit `created_at` field in the `Album` model, inherit from [`TimeStampedModel`]
class TimeStampedModel(models.Model):
     creation_datetime = models.DateTimeField(auto_now_add=True)
     class Meta:
         abstract = True
class Album(TimeStampedModel):
    artist_name=models.ForeignKey(Artist,on_delete=models.CASCADE )
    name = models.CharField(max_length=100 ,default="New Album")
   # creation_datetime=models.DateTimeField()
    release_datetime=models.DateTimeField(blank=False)
    cost= models.DecimalField( blank=False, decimal_places=3 , max_digits=20)
    #..1 adding is_approved field 
    is_approved=models.BooleanField(default=False)
    def __str__(self):
        return self.name
