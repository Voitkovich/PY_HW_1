
class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def calc_length(self):
        return 2 * pi * self.radius

    def calc_square(self):
        return pi * self.radius**2


c1 = Circle(4.5)
print(c1.radius)
print(c1.calc_length(1))
print(c1.calc_square())

