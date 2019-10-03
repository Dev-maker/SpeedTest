from django.contrib.gis import admin
from .models import Data

admin.site.register(Data, admin.GeoModelAdmin)
