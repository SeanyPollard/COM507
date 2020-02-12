from com507.simulation.model.agent import Agent
from com507.simulation.model.location import Location
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