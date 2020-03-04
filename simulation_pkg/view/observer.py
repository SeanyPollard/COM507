from abc import ABC, abstractmethod

class Observer(ABC):
    
    @abstractmethod
    def add_observer(self):
        pass

    @abstractmethod
    def remove_observer(self):
        pass

    @abstractmethod
    def notify_observers(self):
        pass