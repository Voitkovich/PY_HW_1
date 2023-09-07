# Создайте функцию-замыкание, которая запрашивает два целых числа:
# от 1 до 100 для загадывания,
# от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль
# просит угадать загаданное число за указанное число попыток.
from typing import Callable


def game(num: int, tries: int) -> Callable:

    def guessing() -> bool:
        count = 0
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
    return guessing


if __name__ == "__main__":
    round_game = game(num=5, tries=3)
    print(round_game())