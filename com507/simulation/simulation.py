from .config import Config
from abc import abstractmethod
from time import sleep

class Simulation:
    def __init__(self):
        self._is_running = False
        self._speed = Config.initial_sim_speed
        self._step = 0

    @abstractmethod
    def _prepare(self):
        pass

    @abstractmethod
    def _render(self):
        pass

    @abstractmethod
    def _reset(self):
        pass

    @abstractmethod
    def _update(self):
        print("This worked")

    def run(self):
        self._is_running = True
        self._prepare()

        while self._is_running == True:
            self._update()
            self._render()
            sleep(self.__sleep_calc())
            self._is_running = False

    def __sleep_calc(self):
        return Config.max_sim_speed - self._speed

    