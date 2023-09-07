# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат,
# который она возвращает.
# При повторном вызове файл должен расширяться,
# а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию,
# которая может принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.
import json
from typing import Callable


def json_logging(func: Callable):
    try:
        with open(f'{func.__name__}.json', 'r') as data:
            result_list = json.load(data)
    except FileNotFoundError:
        result_list = []

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result_list.append({'args': args,
                            **kwargs,
                            'result': result})
        with open(f'{func.__name__}.json', 'w') as data:
            json.dump(result_list, data, indent=4)
        return result
    return wrapper


@json_logging
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


@json_logging
def sum_args(*args, **kwargs):
    return sum(args)


if __name__ == "__main__":
    guessing(num=3, tries=2)
    sum_args(1, 2, 3, revers='Yes')