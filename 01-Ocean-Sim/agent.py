from location import Location
from abc import ABC

class Agent(ABC):
    def __init__(self, location:Location):
        self.location = location

    def get_location(self):
        return self.location

    def set_location(self, location:Location):
        self.location = location
