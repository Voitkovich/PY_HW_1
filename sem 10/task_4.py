# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод,
# выводящий информацию специфичную для данного класса.

class Animal:
    def __init__(self, name: str, age):
        self.name = name.capitalize()
        self.age = age

class Dogs(Animal):

    def __init__(self, name: str, age, color, type_, size):
        super().__init__(name, age)      
        self.color = color
        self.type = type_
        self.size = size

    def get_specific(self):
        return f"{self.color} {self.type} {self.size}"    
    

class Birds(Animal):
        
    def __init__(self, name: str, age: int, flight: bool, swimming: bool):
        super().__init__(name, age)
        self.flight = flight
        self.swimming = swimming
        
    def show(self)-> None:
        print(f'Летает - {self.flight}, плавает - {self.swimming}')


class Fish(Animal):

    def __init__(self, name: str, age, habitation, view ):
        super().__init__(name, age)
        self.habitation = habitation
        self.view = view

    def specific_fish(self):
        return f'{self.habitation}, {self.view}'
    
fish = Fish('Окунь', '1','Речная','Хищник')  
dogs = Dogs("Шарик", "11", "Рыжий", "Корги", "Большой")
bird = Birds("Ворона", "15", "Много", "Мало")
print(fish.specific_fish())
print(bird.show())
print(dogs.get_specific())


