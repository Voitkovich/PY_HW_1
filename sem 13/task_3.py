# Создайте класс с базовым исключением и дочерние классы-исключения: 
# ошибка уровня, ошибка доступа, ошибка проекта

import json

class ProjectException(Exception):
    pass

class ErrorLevel(ProjectException):
    pass

class ErrorPermition(ProjectException):
    pass

class User:
    def __init__(self, name, id, level=0) -> None:
        self.name = name
        self.id = id
        self.level = level
        

    def __eq__(self, __value: "User") -> bool:
       return self.id == __value.id and self.name == __value.name

         

def load_json():
    try:
        with open('data_base.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        return [] 
    result = []
    for level, value in data.items():
        for user in value:
            name,id = user.values()
            result.append(User(name= name, id= id, level= int(level)))
    return result


print(load_json())

# Доработаем задачи 3 и 4.
# Создайте класс проекта, который имеет следующие методы: 
# * загрузка данных (функция из задания 4)



class Project:
    def __init__(self):
        self.data = []
        self.user = None

    def loan_data(self):
        self.data = load_json()



# вход в систему - требует указать имя и id пользователя. 
# Для проверки наличия пользователя в множестве используйте 
# магический метод проверки на равенство пользователей. 
# Если такого пользователя нет, вызывайте исключение доступа. 
# А если пользователь есть, получите его уровень из множества пользователей.     


    def enter(self, name, id):
        user = User(name, id)
        for us in self.data:
            if us == user:
                self.user = us
        else:
            raise ErrorPermition        





