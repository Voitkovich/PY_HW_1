
# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину прямоугольника 
# и встройте контроль недопустимых значений (отрицательных). 
# Используйте декораторы свойств.




class Rectangle:

    __slots__ = ("_width", "_length")


    def __init__(self, _length: float, _width: float = None) -> None:
        self._length = _length
        if _width:
            self._width = _width
        else:
            self._width = _length

    @property
    def width(self):
        return self._width

    @property
    def lenght(self):
        return self._lenght        
    
    @width.setter
    def width(self, new_width):
        self._width = new_width

    @lenght.setter
    def lenght(self, new_lenght):
        self.lenght = new_lenght    


    def perimetr(self):
        return (self._length + self._width) * 2
    
    def ploshad(self):
        return self._length * self._width
    
    def __add__(self, other):
        result = self.perimetr() + other.perimetr()
        _width = self._width + other._width
        lenght = (result // 2) - _width
        return Rectangle(_width, lenght) 
    

    def __sub__(self, other):
        result = self.perimetr() - other.perimetr()
        _width = self._width - other._width
        if _width <= 0:
            raise Exception("Отрицательная ширина")
        lenght = (result // 2) - _width
        if lenght <= 0:
            raise Exception("Отрицательная длинна")
        return Rectangle(_width, lenght)

    
    def __repr__(self):
        return f"Rectangle{self._width, self._length}" 


    def __repr__(self):
        return f"Rectangle{self._width, self._length}"
    
    def __eq__(self, other)-> bool: 
        return self.ploshad() == other.ploshad()
    
    def __gt__(self, other)-> bool: 
        return self.ploshad() > other.ploshad()
    
    def __le__(self, other)-> bool: 
        return self.ploshad() < other.ploshad()


r1 = Rectangle(2)
r2 = Rectangle(4, 2)
r1._width = 3
print(r1._width)


print(r1 < r2)
print(r1 + r2)
# print(r2 - r1)
print(r1.perimetr(), r2.perimetr())
print(r1.ploshad(), r2.ploshad())