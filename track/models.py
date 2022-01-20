
from django.db import models
from album.models import Album
# Create your models here.

class Track(models.Model):
	name = models.CharField(max_length=30)
	gender = models.CharField(max_length=30)
	year = models.CharField(max_length=4)
	album = models.ForeignKey(Album, on_delete=models.PROTECT,
	 related_name='fk_album')
	file = models.FileField(upload_to='track/', null=True)

	def __str__(self):
		return self.name

	def artistFullName(self):
		return self.album.artist.firstName + ' ' + self.album.artist.lastName

	def artistNickName(self):
		return self.album.artist.nickName

	def albumName(self):
		return self.album.name

	class Meta:
		db_table = 'track'