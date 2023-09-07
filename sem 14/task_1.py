# Создайте функцию,
# которая удаляет из текста все символы кроме
# букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

# Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)


from string import ascii_letters

LETTERS = set(ascii_letters) | {' '}


def clear_text(text: str) -> str: # ['a', 'b', 'c'] -> 'abc'
    """
    >>> clear_text('some text')
    'some text'

    >>> clear_text('SoMe TexT')
    'some text'

    >>> clear_text('SoMe, TexT')
    'some text'

    >>> clear_text('some абв text')
    'some text'

    >>> clear_text('Some, абв text')
    'some text'

    >>> clear_text('somehbfhabhbg 12473147ty , aujfgnhasbg') # пояснение
    'somehbfhabhbg ty aujfgnhasbg'

    """
    return ' '.join("".join(i for i in text if i in LETTERS).lower().split())


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)