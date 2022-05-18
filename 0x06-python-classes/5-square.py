#!/usr/bin/python3
"""Contains a class that defines a square.
Initialize each object by the
__init__ method with a private instance variable called
__size that takes the size variable's value passed as
argument. Also checks if the size arg has a valid value.
area method returns the area of the square.
"""


class Square:
    """Class that defines a square"""
    def __init__(self, size=0):
        """__init__ method that initialize the __size attribute"""
        self.size = size

    @property
    def size(self):
        """returns the value of size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size attribute to value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """return the value of the square's area"""
        return self.size ** 2

    def my_print(self):
        """prints the square with #"""
        if self.size == 0:
            print("")
        else:
            for i in range(0, self.size):
                for j in range(0, self.size):
                    print('#', end="")
                print("")
