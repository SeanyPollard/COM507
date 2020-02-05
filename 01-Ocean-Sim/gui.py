from tkinter import *

class Gui(Tk):
    def __init__(self):
        super().__init__()

        self.__add_agent()
        self.__add_envrionment()

    def __location(self):
        self.x = int()
        self.y = int()

    def __add_agent(self):
        self.__location    