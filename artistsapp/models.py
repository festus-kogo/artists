from django.db import models
from datetime import datetime

# Create your models here.
class Artist(models.Model):
    name = models.CharField(unique=True, max_length=200)
    stage_name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    dob = models.DateField()

    @property
    def age(self):
        return int((datetime.now().date() - self.dob).days / 365.25)

    def __str__(self):
        return f"{self.name} ({self.stage_name})"
    
    def get_absolute_url(self):
        return "/artists"

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    release_date = models.DateField()

    @property
    def age(self):
        return int((datetime.now().date() - self.release_date).days / 365.25)

    def __str__(self):
        if len(self.name.split()) <= 2:
            return f"{self.name} album by {self.artist.stage_name}"
        
        return f"{self.name}"
    
    def get_absolute_url(self):
        return "/albums"

class Song(models.Model):
    name = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.CharField(max_length=200, default="")
    
    @property
    def age(self):
        return self.album.age

    def __str__(self):
        if len(self.name.split()) <= 3:
            return f"{self.artist.stage_name} - {self.name}"
        
        return f"{self.name}"
    
    def get_absolute_url(self):
        return "/songs"
