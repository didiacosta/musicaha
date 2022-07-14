from django.contrib import admin
from .models import Artist, Country

# Register your models here.

class AdminCountry(admin.ModelAdmin):
	list_display = ('id','name',)
	search_fields = ('name',)

class AdminArtist(admin.ModelAdmin):
	list_display = ('id','country','firstName','lastName','nickName')
	search_fields = ('firstName','lastName','nickName')
	list_filter=('country',)

admin.site.register(Artist, AdminArtist)
admin.site.register(Country, AdminCountry)
