# Создайте класс-функцию,
# который считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых чисел и их факториалов.

# Доработаем задачу 1. 
# Создайте менеджер контекста, 
# который при выходе сохраняет значения в JSON файл.

import json
import datetime

class Factorial:
    def __init__(self, maxlen: int) -> None:
        self.maxlen = maxlen
        self.__memory = []
        self.history = {}

    def __call__(self, n: int) -> int:
        res = 1
        for i in range(1, n+1):
            res *= i
        self.add_to_memory(res)
        return res

    def add_to_memory(self, num: int):
        if len(self.__memory) >= self.maxlen:
            self.__memory.pop(0)
        self.__memory.append(num)

    def show_history(self):
        return self.__memory

    def __enter__(self):
        try:
            with open('factorial.json', 'r') as data:     
                self.history = json.load(data)

        except FileNotFoundError:
            self.history = {}
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('factorial.json', 'w') as data:
            self.history.update({str(datetime.datetime.now()): self.__memory})
            json.dump(self.history, data, indent= 4)
        

            


if __name__ == '__main__':
    f1 = Factorial(3)
    with f1 as f:
        f(4), f(6), f(8)
        
    print(f1(4), f1(3), f1(2))
    print(f1.show_history())
    print(f1(5))
    print(f1.show_history())