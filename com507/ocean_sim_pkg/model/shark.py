from .fish import Fish
from ...simulation_pkg.model.location import Location
from ...simulation_pkg.model.agent import Agent
from ...simulation_pkg.model.environment import Environment

class Shark(Fish):
    def __init__(self, location:Location):
        super().__init__(location)

    def act(self, environment:Environment):
        self.swim(environment)

    def eat(self, agent:Agent):
        pass

