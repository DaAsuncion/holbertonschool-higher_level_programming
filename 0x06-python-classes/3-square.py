#!/usr/bin/python3
"""Creating a new class"""

class Square:
    """Write a class Square that defines a square by: (based on 2-square.py)"""
    def __init__(self,size=0):
        """Init square with size"""
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """returns square area"""
        return self.__size * self.__size
