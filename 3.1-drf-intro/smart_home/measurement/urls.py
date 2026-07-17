from django.urls import path
from .views import SensorList, SensorCreateView


urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path(r'sensors/',SensorList.as_view()),
    path(r'sensors/add',SensorCreateView.as_view())
]
