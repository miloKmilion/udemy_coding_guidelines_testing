# type: ignore
# ruff: noqa

from functools import total_ordering
from math import sqrt
from typing import Any

# Dunder: Double underscore
@total_ordering
class Vector2D:
    def __init__(self, x: float = 0.0, y: float= 0.0):
        '''This is a summary

        Args:
            x (float, optional): foo. Defaults to 0.0.
            y (float, optional): bar. Defaults to 0.0.
        '''
        self.x = x
        self.y = y

    def __call__(self):
        print("Calling the __call__ method!")

    def __repr__(self):
        return f"vector.Vector2D({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __abs__(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def __eq__(self, other_vector):
        return self.x == other_vector.x and self.y == other_vector.y

    def __lt__(self, other_vector):
        return abs(self) < abs(other_vector)

    def __add__(self, other_vector):
        x = self.x + other_vector.x
        y = self.y + other_vector.y
        return Vector2D(x, y)

    def __sub__(self, other_vector):
        x = self.x - other_vector.x
        y = self.y - other_vector.y
        return Vector2D(x, y)

    def __mul__(self, other):
        if isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        return Vector2D(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector2D(self.x / other, self.y / other)
