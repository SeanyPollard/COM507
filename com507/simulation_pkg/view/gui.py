from ..model.environment import Environment
from ..config import Config
from ..model.location import Location
from tkinter import Tk, Frame, Label, Button, LEFT

class Gui(Tk):
    def __init__(self, environment:Environment):
        super().__init__()

        #environment stuff
        self.__environment = environment

        #GUI components
        self.__add_header_frame()
        self.__add_grid_frame()
        self.__add_footer_frame()

        #Header frame components
        self.__add_legend_label()

        #Grid frame components
        self.__add_grid_labels()

        #Footer frame components
        self.__add_start_button()
        self.__add_step_button()
        self.__add_stop_button()
        self.__add_reset_button()

    def __add_header_frame(self):
        self.__header_frame = Frame()
        self.__header_frame.grid(row = 0, column = 0)

    def __add_legend_label(self):
        self.__legend_label = Label(self.__header_frame)
        self.__legend_label.pack()
        self.__legend_label.configure(text="Sharks")

    def __add_grid_frame(self):
        self.__grid_frame = Frame()
        self.__grid_frame.grid(row = 1, column = 0)

    def __add_grid_labels(self):
        self.__grid_labels = [[None for i in range(Config.WORLD_WIDTH)] for j in range(Config.WORLD_HEIGHT)]
        for row in range(0,Config.WORLD_HEIGHT):
            for col in range(0,Config.WORLD_WIDTH):
                self.__grid_labels[row][col] = Label(self.__grid_frame)
                self.__grid_labels[row][col].grid(row=row, column=col)
                self.__grid_labels[row][col].configure(width=2, height=1, borderwidth=1, relief="groove")
                location = Location(col, row)
                if self.__environment.get_agent(location) != None:
                    self.__grid_labels[row][col].configure(background="red", text="S")
                else:
                    self.__grid_labels[row][col].configure(background="blue", text="")
        

    def __add_footer_frame(self):
        self.__footer_frame = Frame()
        self.__footer_frame.grid(row = 2, column = 0)

    def __add_start_button(self):
        self.__start_button = Button(self.__footer_frame)
        self.__start_button.pack(side=LEFT)
        self.__start_button.configure(text="Start")

    def __add_step_button(self):
        self.__step_button = Button(self.__footer_frame)
        self.__step_button.pack(side=LEFT)
        self.__step_button.configure(text="Step")

    def __add_stop_button(self):
        self.__stop_button = Button(self.__footer_frame)
        self.__stop_button.pack(side=LEFT)
        self.__stop_button.configure(text="Stop")

    def __add_reset_button(self):
        self.__reset_button = Button(self.__footer_frame)
        self.__reset_button.pack(side=LEFT)
        self.__reset_button.configure(text="Reset")   

    def refresh(self, envrionment:Environment):
        for row in range(0,Config.WORLD_HEIGHT):
            for col in range(0,Config.WORLD_WIDTH):
                location = Location(col, row)
                if self.__environment.get_agent(location) != None:
                    self.__grid_labels[row][col].configure(background="red", text="S")
                else:
                    self.__grid_labels[row][col].configure(background="blue", text="")


