from django.db import models

# Create your models here.

class Photo(models.Model):
    title = models.CharField(max_length=200)
    albumId = models.IntegerField()
    url = models.CharField(max_length=200, default=0)
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    color = models.CharField(max_length=10, default=0)

    def update(self, newTitle, newAlbumId):
        self.title = newTitle
        self.albumId = newAlbumId

