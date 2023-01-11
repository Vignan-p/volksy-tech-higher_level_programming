#!/usr/bin/python3
"""class"""


class Square:
    """Square with private instance attribute and instatiation"""
    def __init__(self, size=0):
        """square size"""
        self.__size = size

    def area(self):
        """return area value"""
        return (self.__size * self.__size)
    
    @property
    def size(self):
        """Area of square"""
        return (self.__size)
    
    @size.setter
    def size(self, value):
        """value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
