# Доработаем задачу 2. Сохраняйте в лог файл раздельно: уровень логирования, 
# дату события, имя функции (не декоратора), аргументы вызова, результат


import logging

FORMAT = '{levelname} - {asctime} {msg}'

logging.basicConfig(filename='logger.log', level=logging.INFO, filemode='w', format=FORMAT, style='{')
logger = logging.getLogger(__name__)


def logging_deco(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'Def "{func.__name__}" result: {result}, with args {args}{kwargs}')
        return result

    return wrapper


@logging_deco
def sum(a, b):
    try:
        return a + b
    except  Exception as se:
        logger.error(f'Created this error messege {se}')


print(sum(32, 345))