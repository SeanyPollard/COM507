from ...simulation_pkg.model.agent import Agent
from ...simulation_pkg.model.location import Location
from .ocean import Ocean
from abc import abstractmethod

class Fish(Agent):
    def __init__(self, location:Location):
        super().__init__(location)
    
    def swim(self, location:Location):
        self.free_locations = Ocean.find_free_locations(location)

    @abstractmethod
    def eat(self, agent:Agent):
        pass