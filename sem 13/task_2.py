# Создайте функцию аналог get для словаря. Помимо самого словаря 
# функция принимает ключ и значение по умолчанию. 
# При обращении к несуществующему ключу функция должна возвращать 
# дефолтное значение. Реализуйте работу через обработку исключений.


def dict_by_get(my_dict, key, defolt=None):
    try:
        return my_dict[key]
    except KeyError:
        return defolt
    
if __name__ == '__main__':
    my_dict = {'ключ': 11, 'ключ2': 1112}    
    print(dict_by_get(my_dict, 'eee', 333))
    print(dict_by_get(my_dict, 'ключ', 333))