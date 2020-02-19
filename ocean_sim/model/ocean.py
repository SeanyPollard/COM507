from ...simulation.model.environment import Environment
from ...simulation.model.location import Location
from ...simulation.model.agent import Agent

class Ocean(Environment):    
    def __init__(self, width:int, height:int):
        self.agent_grid = [[None for i in range(width)] for j in range(height)] 

    def get_agent(self, location:Location) -> Agent:
        return self.agent_grid[location.get_y()][location.get_x()]

    def set_agent(self, agent:Agent, location:Location):
        self.agent_grid[location.get_y()][location.get_x()] = agent

    def clear(self, width:int, height:int):
        self.agent_grid = [[None for i in range(width)] for j in range(height)]

    def get_width(self, location:Location) -> int:
        return self.agent_grid[location.get_x()]

    def get_height(self, location:Location) -> int:
        return self.agent_grid[location.get_y()]
