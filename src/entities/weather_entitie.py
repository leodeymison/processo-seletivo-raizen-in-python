import datetime

class WeatherCreate:
    def __init__(self):
        self.temperature
        self.sensation
        self.pressure
        self.humidity
        self.temperature_max
        self.temperature_min

class WeatherResponse:
    def __init__(self, temperature, sensation, pressure, humidity, temperature_max, temperature_min):
        self.id = 7
        self.temperature = temperature
        self.sensation = sensation
        self.pressure = pressure
        self.humidity = humidity
        self.temperature_max = temperature_max
        self.temperature_min = temperature_min
        self.createdAt = datetime.datetime.now()
        self.updatedAt = datetime.datetime.now()

