from django.db import models

# Create your models here.

class Country(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class Artist(models.Model):
	country = models.ForeignKey(Country, related_name="Fk_artist_country", 
		on_delete=models.PROTECT, null=True)
	firstName = models.CharField(max_length=30)
	lastName = models.CharField(max_length=30)
	nickName = models.CharField(max_length=30, null=True, blank=True)

	def __str__(self):
		return self.firstName + ' ' + self.lastName

	class Meta:
		db_table = 'artista'