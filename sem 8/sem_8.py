
# Вспоминаем задачу 3 из прошлого семинара.
# Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый
# с данными в формате JSON. 
# Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки.

import json
import csv


# with open(r'D:\deepening in python\Seminars\Seminar_8\result.txt', 'r') as f:
#     data = f.read().split('\n')[:-1]
# res_list = []
# for note in data:
#     name,mult = note.split()
#     res_list.append({'name': name, 'mult': float(mult)})
# print(res_list)
# with open('res.json', 'w') as r:
#     json.dump(res_list, r, indent = 4)


# Напишите функцию, которая в бесконечном цикле запрашивает имя, 
# личный идентификатор и уровень доступа (от 1 до 7). После каждого ввода 
# добавляйте новую информацию в JSON файл. Пользователи группируются по уровню доступа. 
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.



# def  apdate_data(data):
    
#     name = input('Введите ваше имя: ')
#     id = int(input('Введите ваш айди: '))
#     level = input('Введите ваш уровень доступа: ')
    
#     temp = data.get(level, [])
#     temp.append({'name': name, 'id': id})
#     data[level] = temp
    
#     return data

 

# while True:
    
#     try:
#         with open('data_base.json', 'r') as f:
#             data = json.load(f)
#     except FileNotFoundError:
#         data = {}

#     data = apdate_data(data)

#     with open('data_base.json', 'w') as f:
#         data = json.dump(data, f, indent=4)


# Напишите функцию, которая сохраняет созданный 
# в прошлом задании файл в формате CSV.

with open('data_base.json', 'r') as r:
    data = json.load(r)
    print(data)
    res_list = []
for key, values in data.items():
    for i in values:
        res_list.append({'level': key, 'id': i['id'], 'name': i['name']})




with open('res.csv','w') as res:
    temp = csv.DictWriter(res,
                          fieldnames = ['level','id','name'],
                          delimiter=',')
    temp.writeheader()
    temp.writerows(res_list)
