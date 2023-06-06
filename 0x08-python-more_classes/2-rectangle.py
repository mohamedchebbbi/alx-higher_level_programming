#!/usr/bin/python3
'''Module for Rectangle class'''


class Rectangle:
    '''This class defines a simple Rectangle'''

    def __init__(self, width=0, height=0):
        '''Constructor.

        Args:
            width: The width of rectangle
            height: The height of rectangle
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Property for the width

        Raises:
            TypeError: If width is not integer
            ValueError: If width < 0
        '''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Property for the height

        Raises:
            TypeError: If height not integer
            ValueError: If height  <  0
        '''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Returns area'''
        return self.width * self.height

    def perimeter(self):
        '''Returns perimeter'''
        if not self.width or not self.height:
            return 0
        return (self.width + self.height) * 2
