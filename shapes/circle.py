import math
from .shape import Shape

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Вычисление площади круга по формуле: п * r^2
        return math.pi * self.radius ** 2