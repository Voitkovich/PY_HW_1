# Создайте функцию, которая запрашивает числовые данные
# от пользователя до тех пор, пока он не введёт 
# целое или вещественное число. Обрабатывайте 
# не числовые данные как исключения.

def coreckt_float():

    while True:
        number = input("Введите число: ")
        try:
            return float(number)
        except ValueError:
            print("Введено НЕ число")


if __name__ == '__main__':
    coreckt_float()