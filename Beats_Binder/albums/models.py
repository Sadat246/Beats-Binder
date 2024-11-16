from django.db import models

class Album(models.Model):
	deezer_id = models.IntegerField(unique=True)
	name = models.CharField(max_length=250)
	artist = models.ManyToManyField('artists.Artist', related_name="album_artist")
	cover = models.URLField(max_length=200)
	genre = models.CharField(max_length=50)
	nb_tracks = models.IntegerField()
	duration = models.IntegerField()
	release_date = models.DateField()
	record_type = models.CharField(max_length=50)
	saved = models.BooleanField(default=False)
# Create your models here.
