from ocean import Ocean
from shark import Shark
from location import Location

class Simulation:
    def __init__(self):
        self.ocean = Ocean(2,2)
        self.ocean.set_agent(Shark(Location(0, 1)))
        print(self.ocean.get_agent[0][1])

Simulation()