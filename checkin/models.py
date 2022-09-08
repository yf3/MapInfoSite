from django.db import models

class Map(models.Model):
    title = models.CharField(max_length=128)

class POIType(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return str(self.name)

class Attribute(models.Model):
    name = models.CharField(max_length=128)
    for_type = models.ForeignKey(POIType, on_delete=models.CASCADE, null=False,)
    objects = models.Manager()

    def __str__(self):
        return str(self.name)

class POI(models.Model):
    name = models.CharField(blank=True, default='No Title', max_length=128)
    attachment = models.ImageField(blank=True, null=True)
    poi_type = models.ForeignKey(POIType, on_delete=models.SET_NULL, null=True)
    attributes = models.ManyToManyField(Attribute, blank=True)
    longitude = models.FloatField(default=0)
    latitude = models.FloatField(default=0)
    comment = models.CharField(blank=True, default='', max_length=1000)
    objects = models.Manager()

    def __str__(self):
        return str(self.name)
    