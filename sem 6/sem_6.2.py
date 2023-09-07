# Создайте модуль с функцией внутри. Функция получает на вход загадку, 
# список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки,
# с которой была отгадана загадка или ноль, если попытки исчерпаны.



def riddle_game(riddle = "Зимой и летом одним цветом", 
                riddle_ans = ["Елка", "Eжик", "Зима"],
                tryes = 3):
    
    for i in range(tryes):
        word = input(f"Отгадайте загадку - {riddle}: ")
        if word in riddle_ans:
            return i
    
    return 0




def add_dict_game():

    dict_game = {'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],
             'Не лает, не кусает, в дом не пускает': ['замок'],
             'Сидит дед во сто шуб одет': ['лук', 'луковица'],}
    
    for key, value in dict_game.items():
        riddle_game(key, value, tryes=5)

if __name__ == "__main__":
    add_dict_game()



# Добавьте в модуль с загадками функцию, которая хранит словарь списков. 
# Ключ словаря - загадка, значение - список с отгадками. 
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

#     def add_dict_game():
#     dict_game = {'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],
#                  'Не лает, не кусает, в дом не пускает': ['замок'],
#                  'Сидит дед во сто шуб одет': ['лук', 'луковица'], }

#     for key, value in dict_game.items():
#         _func(riddle_game(key, value, tryes=5), key)

# _dict = {}

# def _func(attempt: int, riddle: str):

#     _dict.update({riddle: attempt})

# def _show_result():

#     for key, value in _dict.items():
#         print(key, value)

# if __name__ == "__main__":
#     add_dict_game()
#     _show_result()    
        