# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class SensorList(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorCreateView(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class RetrieveUpdateSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


