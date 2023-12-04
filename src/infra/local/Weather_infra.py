from ...entities.weather_entitie import WeatherResponse
from ..schemas.weather_repository import WeatherRepositoryModel
import datetime

list = [
    WeatherResponse(1, 273.0, 271.18, 1013, 1015, 274.5, 271.22, datetime.datetime.now(), datetime.datetime.now()),
    WeatherResponse(2, 273.4, 272.68, 1012, 1015, 274.1, 271.22, datetime.datetime.now(), datetime.datetime.now()),
    WeatherResponse(3, 274.2, 271.58, 1015, 1015, 274.2, 271.22, datetime.datetime.now(), datetime.datetime.now()),
    WeatherResponse(4, 272.2, 260.48, 1013, 1015, 274.7, 271.22, datetime.datetime.now(), datetime.datetime.now()),
    WeatherResponse(5, 279.2, 281.78, 1011, 1015, 274.5, 271.22, datetime.datetime.now(), datetime.datetime.now())
]
class WeatherRepository(WeatherRepositoryModel):
    def getAll(self, quantityDays: int):
        return list[-quantityDays:]
