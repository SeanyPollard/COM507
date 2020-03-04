from ...simulation_pkg.model.agent import Agent
from ...simulation_pkg.model.location import Location
from .ocean import Ocean
from abc import abstractmethod
from random import seed, randint

class Fish(Agent):
    def __init__(self, location:Location):
        super().__init__(location)
    
    def swim(self, location:Location):
        seed(1)
        self.free_locations = Ocean.find_free_locations(location)
        self.rng_max = len(self.free_locations)
        self.swim_to = randint(0,self.rng_max)
        print(self.free_locations)

    #@abstractmethod
    #def eat(self, agent:Agent):
    #    pass