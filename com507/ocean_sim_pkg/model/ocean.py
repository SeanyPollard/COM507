from ...simulation_pkg.model.environment import Environment
from ...simulation_pkg.model.location import Location
from ...simulation_pkg.model.agent import Agent
from ...simulation_pkg.config import Config

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

    def world(self, agent:Agent):
        pass

    def find_free_locations(self, location:Location) -> Location:
        self.free_locations = []
        for x in range(-1,2):
            if location.get_x() + x < 0:
                continue
            elif location.get_x() + x >= Config.WORLD_WIDTH:
                continue
            else:
                for y in range(-1,2):
                    if location.get_y() + y < 0:
                        continue
                    elif location.get_y() + y >= Config.WORLD_HEIGHT:
                        continue
                    else:
                        if self.agent_grid[(location.get_y() + y)][(location.get_x() + x)] == None:
                            self.free_locations.append(Location((location.get_x() + x),(location.get_y() + y)))
        return self.free_locations
        