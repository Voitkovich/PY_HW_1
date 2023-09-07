# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для
# увеличения возраста на год,
# full_name для вывода полного ФИО и т.п. на ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого изменения,
# но есть возможность получить текущий возраст.


# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для
# увеличения возраста на год,
# full_name для вывода полного ФИО и т.п. на ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого изменения,
# но есть возможность получить текущий возраст.
from datetime import datetime


class Person:
    def __init__(self,
                 name: str,
                 surname: str,
                 year_birth: int) -> None:
        self.name = name
        self.surname = surname
        self.__age = datetime.now().year - year_birth

    def birthday(self):
        self.__age += 1

    def full_name(self) -> str:
        return f'{self.name} {self.surname}'

    def age(self) -> int:
        return self.__age

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'

    def __add__(self, obj):

        return f'{self.name} += {obj.name}'


p1 = Person('Vlad', 'Isaev', 980)
p2 = Person('Alex', 'Smirnov', 981)
print(p1.age())
print(p1.birthday())
print(p1.age())
print(p1.full_name())
print(p1)
print(p1 + p2)


# Создайте класс Сотрудник.
# Воспользуйтесь классом человека
# из прошлого задания.
# У сотрудника должен быть шестизначный
# идентификационный номер и уровень доступа
# (остаток от суммы цифр id делённой на семь).


from datetime import datetime
from random import randint


class Person:
    def __init__(self,
                 name: str,
                 surname: str,
                 year_birth: int) -> None:
        self.name = name
        self.surname = surname
        self.__age = datetime.now().year - year_birth

    def birthday(self):
        self.__age += 1

    def full_name(self) -> str:
        return f'{self.name} {self.surname}'

    def age(self) -> int:
        return self.__age

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'

    def __add__(self, obj):

        return f'{self.name} += {obj.name}'


class Employee(Person):
    __LOWER_LIM = 100_000
    __UPPER_LIM = 999_999
    __LEVEL_DIV = 7

    def __init__(self,
                 name: str,
                 surname: str,
                 year_birth: int) -> None:
        super().__init__(name, surname, year_birth)
        self.id = randint(self.__LOWER_LIM,
                          self.__UPPER_LIM)

        self.level = sum(map(int, list(str(self.id)))) % self.__LEVEL_DIV


e1 = Employee('Vlad', "Isaev", 980)
e2 = Employee('Alex', 'Smirnov', 981)
print(e1.id, e1.level)
print(e1.id, e1.level)
print(e1 + e2)