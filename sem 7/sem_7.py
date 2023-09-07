# Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел. 
# Первое число int, второе - float разделены вертикальной чертой. 
# Минимальное число - -1000, максимальное - +1000. 
# Количество строк и имя файла передаются как аргументы функции.

from random import randint, uniform



def fil_numb(name, count_str):
    with open(name, 'w') as f:
        for i in range(count_str):    
            f.write(f'{randint(-1000, 1000)}|{uniform(-1000, 1000)}\n')
    

fil_numb('file_txt', 50)


# Напишите функцию, которая генерирует псевдоимена. 
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# Полученные имена сохраните в фай


from random import choice, randint

VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'


def psevdoname_gen():
    rword = ''
    for _ in range(randint(4, 7)):
        rword += choice(VOWELS + CONSONANTS)
    return rword.capitalize()


def add_word(word: str, count_words: int):
    with open(word, 'w') as names_file:
        for _ in range(count_words):
            names_file.write(psevdoname_gen() + "\n")


if __name__ == '__main__':
    add_word('word_list.txt', 5)


# Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами. 
# Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, сколько в более длинном файле. 
# При достижении конца более короткого файла, возвращайтесь в его начало.

from typing import TextIO



def read_file(file: TextIO) -> str:    
    text = file.readline()
    if not text:
        file.seek(0)
        text = file.readline()
    return text[:-1]


def create_mult(file_names: str, file_numbers, result):

    with (open(file_names, 'r') as f_names, 
          open(file_numbers, 'r') as f_numbs, 
          open(result, 'w') as f_res):
        print(f_names.read(), f_numbs.read())      
        
        len_names = len(f_names.readlines())
        len_numbs = len(f_numbs.readlines())
        print(len_names, len_numbs)
        max_file_len = max(len_names, len_numbs)
      

        for _ in range(max_file_len):
            num_1, num_2 = map(float, read_file(f_numbs).split('|'))
            names = read_file(f_names)
            mult = num_1 * num_2

            print(names, mult, max_file_len)

            if mult < 0:
                f_res.write(f"{names.lower()} {abs(mult)}")
            else:
                f_res.write(f"{names.upper()} {int(mult)}")    
            
      

if __name__ == '__main__':
    word_name = 'word_list.txt'
    num_name = 'num_list.txt'


    fil_numb(num_name, 5)
    add_word(word_name, 10)
    create_mult(word_name, num_name, 'result.txt')
