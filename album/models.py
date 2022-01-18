from django.db import models
from artist.models import Artist
# Create your models here.
class Album(models.Model):
	name = models.CharField(max_length=30)
	artist = models.ForeignKey(Artist, on_delete=models.PROTECT, 
		related_name='fk_artist')

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'album'