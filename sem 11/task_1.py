# Создайте класс МояСтрока где будут
# доступны все возможности str и
# дополнительно хранится имя автора строки и время создания (time.time)
from datetime import datetime


class MyStr(str):
    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = datetime.now().time().hour
        return instance


ms1 = MyStr('some text', 'Vladislav')
print(ms1, ms1.author)
print(ms1.time)