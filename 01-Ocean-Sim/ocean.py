from environment import Environment
from location import Location
from agent import Agent

class Ocean(Environment):    
    def __init__(self, width:int, height:int):
        self.agent_grid = [[None for i in range(width)] for j in range(height)] 

    def get_agent(self, location:Location):
        return self.agent_grid[location.get_y()][location.get_x()]

    def set_agent(self, agent:Agent, location:Location):
        self.agent_grid[location.get_y()][location.get_x()] = agent