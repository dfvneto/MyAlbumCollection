from django.db import models

# Create your models here.


class Album(models.Model):
    created = models.DateField()
    name = models.TextField()
    artist = models.TextField()
    class Meta:
        ordering= ['id']

    def __str__(self):
        return self.name
        
class Track(models.Model):
    name = models.TextField()
    length = models.TimeField()
    music_genre = models.TextField()
    album = models.ForeignKey(Album,related_name="tracks", on_delete=models.CASCADE)
    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return self.name