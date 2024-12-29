from rest_framework import serializers
from .models import Garage, Car, Maintenance

class GarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garage
        fields = "__all__"

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"

class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = "__all__"

class MaintenanceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = ["scheduledDate", "serviceType", "car", "garage"]

class MaintenanceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = ["scheduledDate", "serviceType", "car", "garage"]

