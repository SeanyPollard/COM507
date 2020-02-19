from .agent import Agent
from .location import Location
from abc import ABC, abstractmethod

class Environment(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_agent(self, location:Location) -> Agent:
        pass
    
    @abstractmethod
    def set_agent(self, agent:Agent, location:Location):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def get_width(self, width:int) -> int:
        pass

    @abstractmethod
    def get_height(self, height:int) -> int:
        pass    
        
        

