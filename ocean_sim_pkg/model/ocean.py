from ...simulation_pkg.model.environment import Environment
from ...simulation_pkg.model.location import Location
from ...simulation_pkg.model.agent import Agent

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

    def find_free_locations(self, location:Location) -> Location:
# send location to this
# iterate through locations immediately around
# if get y -1 < 0 then ignore
# if get x -1 < 0 then ignore
# if 0,0 then ignore
# if get y +1 > config.world_height then ignore
# if get x +1 > config.world_width then ignore
# if location contains agent then ignore
# else add to list
# return list

        self.free_locations = [if ]
        for i in free_locations[]
        return self.free_locations
        