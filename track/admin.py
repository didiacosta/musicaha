from django.contrib import admin
from .models import Album
from .models import Track

# Register your models here.
class AdminTrack(admin.ModelAdmin):
	list_display = ('id','name','gender','year','album','file', 'artistFullName')
	list_filter = ('album',)
	search_fields = ('name',)

admin.site.register(Track, AdminTrack)
