# На семинаре про декораторы был создан логирующих декоратор. 
# Он сохранял аргументы функции и результат её работы в файл. 
# Напишите аналогичный декоратор, но внутри используйте модуль logging.

import logging


logging.basicConfig(filename= 'logger.log', encoding= 'utf-8', level= logging.INFO, filemode= 'w')
logger = logging.getLogger(__name__)

def logging_deco(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'Результат функции: {result}, с аргументами {args}{kwargs}')
        return result
    return wrapper

@logging_deco
def sum(a, b):
    try:
        return a + b
    except  Exception as se:
        logger.error(f'Возникла такая ошибка {se}')

print(sum(32, "gkgkg"))        



