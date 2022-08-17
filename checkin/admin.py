from django.contrib import admin
from .models import POI, POIType, Attribute, Map

class POITypeAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

# class POIAdmin(admin.ModelAdmin):
#     def formfield_for_manytomany(self, db_field, request, **kawrgs):
#         if db_field.name == 'attributes':
#             kawrgs['queryset'] = Attribute.objects.filter(for_type=)
#         return super(POIAdmin, self).formfield_for_manytomany(db_field, request, **kawrgs)

admin.site.register(Map)
admin.site.register(POI)
admin.site.register(POIType, POITypeAdmin)
admin.site.register(Attribute)
