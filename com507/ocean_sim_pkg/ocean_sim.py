from ..simulation_pkg.simulation import Simulation
from .model.ocean import Ocean
from .model.shark import Shark
from ..simulation_pkg.model.agent import Agent
from ..simulation_pkg.model.location import Location
from ..simulation_pkg.config import Config
from ..simulation_pkg.view.gui import Gui
from random import randint

class Ocean_Simulation(Simulation):
    def __init__(self):
        super().__init__()
    
    def _prepare(self):
        self.ocean = Ocean(Config.WORLD_WIDTH, Config.WORLD_HEIGHT)
        self.agent_list = []
        for y in range(1,Config.WORLD_HEIGHT):
            for x in range(1,Config.WORLD_WIDTH):
                if randint(1,5) == 3:
                    shark = Shark(Location(x,y))
                    self.agent_list.append(shark)
                    self.ocean.set_agent(shark,Location(x,y))

        self.gui = Gui(self.ocean)

    def _render(self):
        self.gui.refresh(self.ocean)
        self.gui.update_idletasks()
        self.gui.update()

    def _reset(self):
        pass

    def _update(self):
        for agent in self.agent_list:
            agent.act(self.ocean)



