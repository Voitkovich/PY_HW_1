# Напишите программу, которая использует модуль 
# logging для вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.


import logging

logging.basicConfig(filename= 'logger.log', encoding= 'utf-8', level= logging.INFO, filemode= 'w')
logger = logging.getLogger(__name__)

def sum(a, b):
    try:
        return a + b
    except  Exception as se:
        logger.error(f'Возникла такая ошибка {se}')


sum(2, 'd')