from django.shortcuts import render
from django.contrib.gis.geos import GEOSGeometry
from .models import *

# Create your views here.
def map(request):        
    if request.method == 'POST':
        multiPolygone= request.POST.get('points')
        multipolygon = GEOSGeometry(multiPolygone, srid=4326)
        wissem=myProject(geomp=multipolygon)
        wissem.save()  
  
    return render(request,'polygone.html')

