from django.contrib.gis.db import models

# Create your models here.
class myProject(models.Model):
    geomp = models.MultiPolygonField(null=True)
    polygon_id = models.BigAutoField(primary_key=True, default=None)