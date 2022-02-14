from .models import Album
from album.models import album
from album.serializers import AlbumLiteSerializer, AlbumSerializer
from rest_framework import serializers

class TrackSerializer(serializers.HyperlinkedModelSerializer):

	album = AlbumLiteSerializer(read_only=True)

	album_id = serializers.PrimaryKeyRelatedField(
		write_only=True, queryset=Album.objects.all())

	class Meta:
		model = Track
		fields = ('id','name','gender','year', 'album_id')

class TrackLiteSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Track
		fields = ('id','name')