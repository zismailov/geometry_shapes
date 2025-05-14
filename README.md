Библиотека для вычисление площади круга по радиусу и треугольника по трем сторонам.

## Требования
- Юнит-тесты
- Легкость добавления других фигур
- Вычисление площади фигуры без знания типа фигуры в compile-time

## Структура проекта:
```bash
geometry_shapes/
│
├── shapes/                   # Пакет с кодом библиотеки
│   ├── __init__.py            # Инициализация пакета
│   ├── shape.py               # Абстрактный класс Shape
│   ├── circle.py              # Класс для круга
│   ├── triangle.py            # Класс для треугольника
│
├── tests/                     # Папка для тестов
│   └── test_shapes.py         # Юнит-тесты для библиотеки
│
├── setup.py                   # Скрипт для установки библиотеки
└── README.md                  # Описание проекта и инструкция
```
## Использование библиотеки:
```python
from shapes.circle import Circle
from shapes.triangle import Triangle

# Создание объекта Circle
circle = Circle(5)
print(circle.area())  # Вывод: 78.54

# Создание объекта Triangle
triangle = Triangle(3, 4, 5)
print(triangle.area())               # Вывод: 6.0
print(triangle.is_right_triangle())  # Вывод: True
```

## Как запустить тесты:
```bash
python3 -m pytest tests
```
