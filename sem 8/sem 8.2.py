import json


def apdate_data(data):
    name = input('Введите ваше имя: ')
    id = int(input('Введите ваш айди: '))
    level = input('Введите ваш уровень доступа: ')

    temp = data.get(level, [])
    temp.append({'name': name, 'id': id})
    data[level] = temp

    return data


while True:
    try:
        with open('data_base.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    data = apdate_data(data)

    with open('data_base.json', 'w') as f:
        data = json.dump(data, f, indent=4)