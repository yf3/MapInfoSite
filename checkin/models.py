from django.db import models

class Map(models.Model):
    title = models.CharField(max_length=128)
    center_lng = models.FloatField(default=0)
    center_lat = models.FloatField(default=0)
    objects = models.Manager()

    def __str__(self) -> str:
        return str(self.title)

class POIType(models.Model):
    name = models.CharField(max_length=128)
    map_id = models.ForeignKey(to=Map, on_delete=models.CASCADE, null=False)
    objects = models.Manager()

    def __str__(self) -> str:
        return str(self.name)

class POI(models.Model):
    map_id = models.ForeignKey(to=Map, on_delete=models.CASCADE, null=False)
    name = models.CharField(blank=True, default='No Title', max_length=128)
    attachment = models.ImageField(blank=True, null=True)
    poi_type = models.ForeignKey(POIType, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    longitude = models.FloatField(default=0)
    latitude = models.FloatField(default=0)
    comment = models.CharField(blank=True, default='', max_length=1000)
    objects = models.Manager()

    def __str__(self) -> str:
        return str(self.name)
