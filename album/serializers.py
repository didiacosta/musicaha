from .models import Album
from artist.models import Artist
from artist.serializers import ArtistLiteSerializer, ArtistSerializer
from rest_framework import serializers

class AlbumSerializer(serializers.HyperlinkedModelSerializer):

	artist = ArtistLiteSerializer(read_only=True)

	artist_id = serializers.PrimaryKeyRelatedField(
		write_only=True, queryset=Artist.objects.all())

	class Meta:
		model = Album
		fields = ('id','name','cover','artist', 'artist_id')

class AlbumLiteSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Album
		fields = ('id','name')