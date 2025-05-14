import pytest
from shapes.circle import Circle
from shapes.triangle import Triangle

# Тест для вычисления площади круга
def test_circle_area():
    circle = Circle(5)  # Создаем круг с радиусом 5
    # Проверяем, что площадь круга близка к ожидаемому значению
    assert circle.area() == pytest.approx(78.53981633974483, rel=1e-5)

# Тест для вычисления площади треугольника
def test_triangle_area():
    triangle = Triangle(3, 4, 5)  # Создаем прямоугольный треугольник
    # Проверяем, что площадь треугольника равна 6
    assert triangle.area() == 6.0

# Тест для проверки, является ли треугольник прямоугольным
def test_right_triangle():
    triangle = Triangle(3, 4, 5)  # Прямоугольный треугольник
    # Проверяем, что треугольник прямоугольный
    assert triangle.is_right_triangle() is True

# Тест для проверки, что треугольник не является прямоугольным
def test_non_right_triangle():
    triangle = Triangle(5, 6, 7)  # Треугольник, не прямоугольный
    # Проверяем, что треугольник не прямоугольный
    assert triangle.is_right_triangle() is False

# Тест для универсальной функции вычисления площади
def test_calculate_area():
    circle = Circle(3)  # Круг с радиусом 3
    triangle = Triangle(3, 4, 5)  # Прямоугольный треугольник
    # Проверяем, что площадь круга и треугольника вычисляются правильно
    assert calculate_area(circle) == pytest.approx(28.274333882308138, rel=1e-5)
    assert calculate_area(triangle) == 6.0

# Тест для проверки, является ли треугольник прямоугольным
def test_triangle_is_right():
    t = Triangle(3, 4, 5)
    assert t.is_right_triangle() is True

    t2 = Triangle(5, 5, 5)
    assert t2.is_right_triangle() is False

# Функция для вычисления площади фигуры без знания ее типа
def calculate_area(shape):
    return shape.area()