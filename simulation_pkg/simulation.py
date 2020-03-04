from .config import Config
from abc import ABC, abstractmethod
from time import sleep

class Simulation(ABC):
    def __init__(self):
        self._is_running = False
        self._speed = Config.INITIAL_SIM_SPEED
        self._step = 0

    @abstractmethod
    def _prepare(self) -> None:
        pass

    @abstractmethod
    def _render(self) -> None:
        pass

    @abstractmethod
    def _reset(self) -> None:
        pass

    def run(self) -> None:
        self._is_running = True
        self._prepare()

        while self._is_running == True:
            self._update()
            self._render()
            sleep(self.__sleep_calc())

    def __sleep_calc(self) -> int:
        return Config.MAX_SIM_SPEED - self._speed

    @abstractmethod
    def _update(self) -> None:
        pass

    