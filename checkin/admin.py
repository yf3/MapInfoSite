from django.contrib import admin
from .models import POI, POIType, Map

class POITypeAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class MapAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Map, MapAdmin)
admin.site.register(POI)
admin.site.register(POIType, POITypeAdmin)
