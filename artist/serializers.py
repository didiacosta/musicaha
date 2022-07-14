from .models import Artist, Country
from rest_framework import serializers


class CountrySerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Country
		fields = ('id','name')

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
	country = CountrySerializer(read_only=True)
	country_id = serializers.PrimaryKeyRelatedField(
		write_only=True, queryset=Country.objects.all())
	class Meta:
		model = Artist
		fields = ('id','firstName','lastName','nickName', 'country', 'country_id')

class ArtistLiteSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Artist
		fields = ('id','nickName')