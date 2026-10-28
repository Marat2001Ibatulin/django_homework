from django.urls import path
from .views import SensorList, SensorCreateView, RetrieveUpdateSensorView, MeasurementCreateView


urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path(r'sensors/',SensorList.as_view()),
    path(r'sensors/add/',SensorCreateView.as_view()),
    path(r'sensors/<pk>/', RetrieveUpdateSensorView.as_view()),
    path(r'measurements/add/',MeasurementCreateView.as_view())
]
