from django.contrib import admin
from .models import Car,Garage


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('unique_id', 'production_year', 'make', 'model', 'license_plate')
    search_fields = ('unique_id', 'make', 'model', 'license_plate')


@admin.register(Garage)
class GarageAdmin(admin.ModelAdmin):
    list_display = ('unique_id', 'name', 'location', 'city', 'capacity')