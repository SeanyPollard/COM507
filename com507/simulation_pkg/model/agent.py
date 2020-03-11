from .location import Location
from abc import ABC, abstractmethod


class Agent(ABC):
    def __init__(self, location:Location):
        self._location = location
        self._alive = True

    @abstractmethod
    def act(self, environment) -> None:
        pass

    def get_location(self) -> Location:
        return self._location

    def is_alive(self, status:bool = None) -> bool:
        if status != None:
            self._alive = status
            
        return self._alive

    def set_location(self, location:Location) -> None:
        self._location = location