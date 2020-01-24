"""Abstract classes"""
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimiter(self):
        pass               # 1,deny other users to create a instance of shape class
                                           # user must impliment methods in subclass


class Square(Shape):
    def __init__(self, side):
        self.__side = side

        def area(self):
            return self.__side * self.__side

        def perimiter(self):
            return 4 * self.__side


square = Square(5)
print(square.area())
print(square.perimiter())



