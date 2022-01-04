from django.contrib import admin
from .models import Place

class PlaceAdmin(admin.ModelAdmin):
    fields = ['name', 'log','lat',"timestamp"]

admin.site.register(Place, PlaceAdmin)