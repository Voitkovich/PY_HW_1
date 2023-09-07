# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные
# в функцию-угадайку числа в диапазоны [1, 100] и [1, 10]. Если не входят,
# вызывать функцию со случайными числами из диапазонов.
from random import randint


def game_deco(func: callable) -> callable:

    def wrapper(num, tries, *args, **kwargs):
        if not 1 <= num <= 100:
            num = randint(1, 100)
        if not 1 <= tries <= 10:
            tries = randint(1, 10)
        return func(num, tries)
    return wrapper


@game_deco
def guessing(num, tries) -> bool:
    count = 0
    print(num, tries)
    while count < tries:
        user_choice = int(input())
        count += 1
        if user_choice == num:
            return True
        elif user_choice < num:
            print('Число больше')
        else:
            print('Число меньше')
    return False


if __name__ == "__main__":
    guessing(101, 47)