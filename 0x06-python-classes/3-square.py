#!/usr/bin/python3
""" This module creates a square that has size."""


class Square:
    """ This is a class which defines a class with some
        definate size."""

    def __init__(self, size=0):
        """ This method intializes a square instance/object
        with an integer value size greater or equal to zero."""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """ Calculates and returns tha area of the square object"""
        return (self.__size ** 2)
