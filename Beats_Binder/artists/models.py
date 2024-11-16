from django.db import models

class Artist(models.Model):
	deezer_id = models.IntegerField(unique=True)
	name = models.CharField(max_length=100)
	cover = models.URLField(max_length=200)
	nb_album = models.IntegerField(default=0)
	saved = models.BooleanField(default=False)
# Create your models here.

# Create your models here.
