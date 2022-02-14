from django.db import models
from django.utils.html import format_html
from artist.models import Artist

# Create your models here.
class Album(models.Model):
	name = models.CharField(max_length=30)
	artist = models.ForeignKey(Artist, on_delete=models.PROTECT, 
		related_name='fk_artist')
	cover = models.ImageField(upload_to='album/', default='album/default.png')

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'album'

	def img_album(self):
		if self.cover:
			return format_html(
				'<img src="{}" width="100" height="100"/>'.
				format(str(self.cover.url)))
		else:
			return None

	img_album.allow_tags = True