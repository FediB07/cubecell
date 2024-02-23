from django.shortcuts import render
# from .models import GeoMap
# from django.contrib.gis.geos import GEOSGeometry
from .mqtt_client import send_to_web

def ma_vue(request):
    context={'data':send_to_web()}
    # if request.method == 'post ':
    #     multipolygone = request.POST.get('polygon')
    #     multipolygon=GEOSGeometry(multipolygone,srid=4326)
    #     project=GeoMap(geomp=multipolygon)
    #     project.save()
    
    return render(request, "website/index.html",context=context)