#!/usr/bin/python3
"""class"""


class Square:
    """square size"""
        self.__size = size

    def size(self):
        """Area of square"""
        return (self.__size)

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return area value"""
        return (self.__size * self.__size)
