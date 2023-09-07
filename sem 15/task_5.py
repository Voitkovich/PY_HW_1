# Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# Преобразуйте его в дату в текущем году. Логируйте ошибки, если текст не соответсвует формату.

import datetime
import argparse

_WEEK = {
    "понедельник": 1,
    "вторник": 2,
    "среда": 3,
    "четверг": 4,
    "пятница": 5,
    "суббота": 6,
    "воскресенье": 7,
}
_WEEK_R = {
    1: "понедельник",
    2: "вторник",
    3: "среда",
    4: "четверг",
    5: "пятница",
    6: "суббота",
    7: "воскресенье",
}

_MOUNTH = {'': 0, 'Января': 1, 'Февраля': 2,
               'Марта': 3, 'Апреля': 4, 'Мая': 5,
               'Июня': 6, 'Июля': 7, 'Августа': 8,
               'Сентября': 9, 'Октября': 10, 'Ноября': 11, 'Декабря': 12}

_MOUNTH_R = dict(map(lambda x: (x[1], x[0]), _MOUNTH.items()))


def convert(text: str):
    """Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
       Преобразуйте его в дату в текущем году. Логируйте ошибки, если текст не соответсвует формату.
    """
    week_count, week_day, mounth = text.split()
    week_count = int(week_count[0])

    week_day = _WEEK[week_day.lower()] - 1
    mounth = _MOUNTH[mounth.capitalize()]
    count_matches = 0

    for day in range(1, 32):
        date_temp = datetime.datetime(datetime.datetime.now().year, mounth, day)
        if date_temp.weekday() == week_day:
            count_matches += 1
            if count_matches == week_count:
                return date_temp

def parser():
    pars = argparse.ArgumentParser(prog= 'convert()')
    pars.add_argument('-wc', default= 1)
    pars.add_argument('-wd', default= datetime.datetime.now().weekday())
    pars.add_argument('-mo', default= datetime.datetime.now().month)
    args = pars.parse_args()
    return convert(f'{args.wc} {_WEEK_R[int(args.wd)]} {_MOUNTH_R[int(args.mo)]}')
    
if __name__ == '__main__':
    print(parser())