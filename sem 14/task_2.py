# Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

from string import ascii_letters
import unittest

LETTERS = set(ascii_letters) | {' '}

def clear_text(text: str) -> str:
    return ' '.join("".join(i for i in text if i in LETTERS).lower().split())


class TestClearText(unittest.TestCase):
    def test_no_change(self):
        self.assertEqual(clear_text('some text'), 'some text')

    def test_registre_change(self):
        self.assertEqual(clear_text('SoMe TexT'), 'some text')

    def test_punctuation_delete(self):
        self.assertEqual(clear_text('SoMe, TexT'), 'some text',
        "Неправильная работа с пунктуацией")


if __name__ == "__main__":
    unittest.main(verbosity=2)