class Location:
    def __init__(self, x:int, y:int):
        self.__x = x
        self.__y = y

    def get_x(self) -> int:
        return self.__x
    
    def set_x(self, x:int) -> None:
        self.__x = x

    def get_y(self) -> int:
        return self.__y

    def set_y(self, y:int) -> None:
        self.__y = y

        