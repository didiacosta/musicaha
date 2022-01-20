
from django.db import models
from album.models import Album
# Create your models here.

class Track(models.Model):
	name = models.CharField(max_length=30)
	gender = models.CharField(max_length=30)
	year = models.CharField(max_length=4)
	name_album = models.ForeignKey(Album, on_delete=models.PROTECT, related_name='fk_album')

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'track'