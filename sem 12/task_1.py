# Создайте класс-функцию,
# который считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых чисел и их факториалов.

class Factorial:
    def __init__(self, maxlen: int) -> None:
        self.maxlen = maxlen
        self.__memory = []

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


if __name__ == '__main__':
    f1 = Factorial(3)
    print(f1(4), f1(3), f1(2))
    print(f1.show_history())
    print(f1(5))
    print(f1.show_history())