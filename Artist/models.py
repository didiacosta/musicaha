from django.db import models

# Create your models here.
class Artist(models.Model):
	firstName = models.CharField(max_length=30)
	lastName = models.CharField(max_length=30)
	nickName = models.CharField(max_length=30, null=True, blank=True)

	def __str__(self):
		return self.firstName + ' ' + self.lastName

	class Meta:
		db_table = 'artista'