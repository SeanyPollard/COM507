from .fish import Fish
from ...simulation_pkg.model.location import Location
from ...simulation_pkg.model.agent import Agent

class Shark(Fish):
    def __init__(self, location:Location):
        super().__init__(location)

    def act(self):
        pass
    
    def swim(self, location:Location):
        super().set_location(location)

    #def eat(self, agent:Agent):
    #    pass

