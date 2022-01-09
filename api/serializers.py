from rest_framework import serializers
from .models import *



class TelemetricDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TelemetricData
        fields = [
            'id',
            'engine_temperature',
            'car_speed',
            'car_gps_lat',
            'car_gps_lon',
            'fuel_consumption_rate',
            'accelerometer',
            'steering_angle',
            'last_updated',
        ]