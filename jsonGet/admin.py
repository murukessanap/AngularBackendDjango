from django.contrib import admin
from .models import StockM

admin.register(StockM)(admin.ModelAdmin)