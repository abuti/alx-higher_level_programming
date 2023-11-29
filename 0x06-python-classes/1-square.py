#!/usr/bin/python3
""" Square with size

This module depicts how to initialize a class object
and how to use private instances."""


class Square:
    """This is a class that defines a square with size."""

    def __init__(self, size):
        """Initializes a square with size"""
        self.__size = size
