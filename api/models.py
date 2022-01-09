from django.db import models


class TelemetricData(models.Model):

    engine_temperature = models.CharField('Engine Temperature', max_length=225)
    car_speed = models.CharField('Car Spedd', max_length=225)
    car_gps_lat = models.CharField('Car GPS Latitide', max_length=225)
    car_gps_lon = models.CharField('Car GPS Longitude', max_length=225)
    fuel_consumption_rate = models.CharField('Fuel Consumption Rate', max_length=225)
    accelerometer = models.CharField('Car Accelerometer', max_length=225)
    steering_angle = models.CharField('Car Steering Angle', max_length=225)
    
    last_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Telemetric data created on {self.date_created}'

