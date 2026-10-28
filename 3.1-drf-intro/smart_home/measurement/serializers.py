from .models import Sensor, Measurement
from rest_framework import serializers

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor_number','temperature', 'created_at', 'image']

class MeasurementDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'image']

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementDataSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
