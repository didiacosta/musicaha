from django.contrib import admin
from .models import Album

# Register your models here.
class AdminAlbum(admin.ModelAdmin):
	list_display = ('id','name','artist', 'img_album')
	list_filter = ('artist',)
	search_fields = ('name',)

admin.site.register(Album, AdminAlbum)
