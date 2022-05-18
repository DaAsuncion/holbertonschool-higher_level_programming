#!/usr/bin/python3
"""Contains a class that defines a square.
__size takes the size variable´s value passed as
argument and checks if the size arg has a valid
value"""


class Square:
    """def a square"""
    def __init__(self, size=0):
        """init"""
        self.__size = size

        @property
        def size(self):
            return self.__size

        @size.setter
        def size(self,value):
            """set size to value"""

            if type(value) is not int:
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

                def area(self):
                    """value of area"""
                    return self.__size ** 2
