from ..simulation_pkg.simulation import Simulation
from .model.ocean import Ocean
from .model.shark import Shark
from ..simulation_pkg.model.location import Location

class Ocean_Simulation(Simulation):
    def __init__(self):
        super().__init__()
        self.ocean = Ocean(2, 2)
    
    def _prepare(self):
        self.ocean.set_agent(Shark(Location(0, 1)), Location(0, 1))

    def _render(self):
        print(self.ocean.get_agent(Location(0, 1)))

    def _reset(self):
        pass

    def _update(self):
        self.ocean.set_agent(None, Location(0, 1))
        self.ocean.set_agent(Shark(Location(1, 0)), Location(1, 0))
