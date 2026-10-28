from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(default='')

class Measurement(models.Model):
    sensor_number = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
    image = models.ImageField(upload_to='measurements/', null=True, blank=True)

