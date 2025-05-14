import math
from .shape import Shape

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        if not self._is_valid_triangle():
            raise ValueError("Стороны не образуют треугольник")

    def _is_valid_triangle(self):
        # Проверка существования треугольника
        return (
            self.a + self.b > self.c and
            self.a + self.c > self.b and
            self.b + self.c > self.a
        )
    
    def area(self):
        # Вычисление площади треугольника по формуле Герона
        s = (self.a + self.b + self.c) / 2
        # Площадь = √(s * (s - a) * (s - b) * (s - c))
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_triangle(self):
        sides = sorted([self.a, self.b, self.c])  # Сортируем стороны по возрастанию
        # Проверяем, выполняется ли a^2 + b^2 = c^2
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)