from agent import Agent
from location import Location
from abc import abstractmethod

class Fish(Agent):
    def __init__(self, location:Location):
        super(location)
    
    @abstractmethod
    def swim(self, location:Location):
        pass

    @abstractmethod
    def eat(self, agent:Agent):
        pass