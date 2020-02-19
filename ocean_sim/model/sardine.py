from .fish import Fish
from ...simulation.model.location import Location

class Sardine(Fish):
    def __init__(self, location:Location):
        super().__init__(location)

    def swim(self, location:Location):
        super().set_location(location)

    def eat(self, agent):
        pass