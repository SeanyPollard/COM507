from .agent import Agent
from .location import Location
from abc import ABC, abstractmethod

class Environment(ABC):
    @abstractmethod
    def clear(self) -> None:
        pass

    @abstractmethod
    def get_agent(self, location:Location) -> Agent:
        pass

    @abstractmethod
    def get_width(self, width:int) -> int:
        pass

    @abstractmethod
    def get_height(self, height:int) -> int:
        pass    
        
    @abstractmethod
    def set_agent(self, agent:Agent, location:Location) -> None:
        pass        