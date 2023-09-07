# Дорабатываем класс прямоугольник из прошлого семинара. 
# Добавьте возможность сложения и вычитания. 
# При этом должен создаваться новый экземпляр прямоугольника. 
# Складываем и вычитаем периметры, а не длинну и ширину. 
# При вычитании не допускайте отрицательных значений


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
    
    def __add__(self, other):
        result = self.perimetr() + other.perimetr()
        width = self.width + other.width
        lenght = (result // 2) - width
        return Rectangle(width, lenght) 
    

    def __sub__(self, other):
        result = self.perimetr() - other.perimetr()
        width = self.width - other.width
        if width <= 0:
            raise Exception("Отрицательная ширина")
        lenght = (result // 2) - width
        if lenght <= 0:
            raise Exception("Отрицательная длинна")
        return Rectangle(width, lenght)

    
    def __repr__(self):
        return f"Rectangle{self.width, self.length}" 


    def __repr__(self):
        return f"Rectangle{self.width, self.length}"
    
    def __eq__(self, other)-> bool: 
        return self.ploshad() == other.ploshad()
    
    def __gt__(self, other)-> bool: 
        return self.ploshad() > other.ploshad()
    
    def __le__(self, other)-> bool: 
        return self.ploshad() < other.ploshad()


r1 = Rectangle(2)
r2 = Rectangle(4, 2)

print(r1 < r2)
print(r1 + r2)
print(r2 - r1)
print(r1.perimetr(), r2.perimetr())
print(r1.ploshad(), r2.ploshad())
