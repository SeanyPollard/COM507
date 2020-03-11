from ...simulation_pkg.model.agent import Agent
from ...simulation_pkg.model.location import Location
from .ocean import Ocean
from abc import abstractmethod
from random import randint

class Fish(Agent):
    def __init__(self, location:Location):
        super().__init__(location)
    
    def swim(self, ocean:Ocean):
        self.free_locations = ocean.find_free_locations(self.get_location())

        if len(self.free_locations) != 0:   
            self.rng_max = len(self.free_locations) - 1
            self.swim_to = randint(0,self.rng_max)
            ocean.set_agent(None,super().get_location())
            super().set_location(self.free_locations[self.swim_to])
            ocean.set_agent(self,self.free_locations[self.swim_to])


    #@abstractmethod
    #def eat(self, agent:Agent):
    #    pass