from .models import Artist
from rest_framework import serializers

class ArtistSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Artist
		fields = ('id','firstName','lastName','nickName')

class ArtistLiteSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Artist
		fields = ('id','nickName')