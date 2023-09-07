# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1. Если передан один параметр, также считаем start=1.

class Gen:
    def __init__(self, stop, start=1, step=1):
        self.start = start
        self.step = step
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        print(self.start, "*")

        while self.start <= self.stop:
            res = 1
            for i in range(1, self.start+1):
                res *= i
            self.start += self.step
            return res
        raise StopIteration
    
        
if __name__ == '__main__':
    exemplar2 = Gen(5)
    for i in exemplar2:
        print(i)