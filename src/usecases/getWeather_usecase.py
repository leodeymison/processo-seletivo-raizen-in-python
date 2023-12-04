from ..infra.schemas.weather_repository import WeatherRepositoryModel

class UseCaseGetWeather:
    def __init__(self, repository: WeatherRepositoryModel):
        self.repository = repository

    def exec(self, quantityDays: int):
        response = self.repository.getAll(quantityDays)
        return response