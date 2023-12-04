from abc import ABC, abstractmethod

class WeatherRepositoryModel(ABC):
    @abstractmethod
    def getAll(self, quantityDays: int):
        pass