# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader. Дополните id до 10
# цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл,
# где каждая строка csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.



import json


with open('res.csv', 'r') as file:
    data = file.read().split('\n\n')[:-1]
print(data)

data = list(map(lambda x: x.split(','), data))
print(data)

result_list = []
for d in data[1:]:
    level, id, name = d
    result_list.append({
        'level': level,
        'id': f'{int(id):010}',
        'name': name.capitalize(),
        'hash': hash(id + name)
    })

with open('users.json', 'w') as db:
    json.dump(result_list, db, indent=4)


