from agent import Agent
from abc import ABC, abstractmethod

class Environment(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_agent(self, location):
        pass
    
    @abstractmethod
    def set_agent(self, location, agent):
        pass
        
        

