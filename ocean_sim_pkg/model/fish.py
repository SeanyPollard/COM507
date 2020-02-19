from ...simulation_pkg.model.agent import Agent
from ...simulation_pkg.model.location import Location
from abc import abstractmethod

class Fish(Agent):
    def __init__(self, location:Location):
        super().__init__(location)
    
    @abstractmethod
    def swim(self, location:Location):
        pass

    @abstractmethod
    def eat(self, agent:Agent):
        pass