from django.contrib import admin
from .models import Album, Track
# Register your models here.


class TrackInline(admin.TabularInline):
        model = Track

class AlbumAdmin(admin.ModelAdmin):
    inlines = [TrackInline, ]


admin.site.register(Album, AlbumAdmin)
admin.site.register(Track)
