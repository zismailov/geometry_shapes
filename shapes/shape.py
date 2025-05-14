# Это абстрактный базовый класс, который будет использоваться для всех фигур.

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this method")