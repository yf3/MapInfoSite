from django.contrib import admin
# from django.db.models import F
from .models import POI, POIType, Map

class POITypeAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class MapAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class POIAdmin(admin.ModelAdmin):
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == 'poi_type':
    #         kwargs['queryset'] = POIType.objects.filter(map_id=1)
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)
    pass

admin.site.register(Map, MapAdmin)
admin.site.register(POI, POIAdmin)
admin.site.register(POIType, POITypeAdmin)
