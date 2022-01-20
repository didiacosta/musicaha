from django.contrib import admin
from .models import Artist

# Register your models here.
class AdminArtist(admin.ModelAdmin):
	list_display = ('id','firstName','lastName','nickName')
	search_fields = ('firstName','lastName','nickName')

admin.site.register(Artist, AdminArtist)

