# Создайте класс прямоугольник.
# Класс должен принимать длину и
# ширину при создании экземпляра.
# У класса должно быть два метода,
# возвращающие периметр и площадь.
# Если при создании экземпляра передаётся
# только одна сторона, считаем что у нас квадрат.


class Rectangle:
    def __init__(self, length: float, width: float = None) -> None:
        self.length = length
        if width:
            self.width = width
        else:
            self.width = length
    def perimetr(self):
        return (self.length + self.width) * 2
    
    def ploshad(self):
        return self.length * self.width

r1 = Rectangle(2)
r2 = Rectangle(4, 2)
print(r1.perimetr(), r2.perimetr())
print(r1.ploshad(), r2.ploshad())