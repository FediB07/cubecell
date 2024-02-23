from django.db import models
# from django.contrib.gis.db import models as gis_models

class Data(models.Model):
    donnée = models.CharField(max_length=500)

# class GeoMap(gis_models.Model):
#     id_polygon = models.AutoField(primary_key=True)
#     geomap = gis_models.MultiPolygonField(null=True)
