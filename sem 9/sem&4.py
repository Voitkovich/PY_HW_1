# Создайте декоратор с параметром.
# Параметр - целое число,
# количество запусков декорируемой функции.
from task3 import json_logging
from functools import wraps

# def many_launch(count: int):
#     def deco(func: callable):
#         def wrapper(*args, **kwargs):
#             res_lst = []
#             for _ in range(count):
#                 res_lst.append(func(*args, **kwargs))
#             return res_lst
#         return wrapper
#     return deco


def many_launch(count: int):
    def deco(func: callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res_lst = []
            for s_c in range(count):
                res_lst.append(func(*[i for i in range(s_c)], **kwargs))
            return res_lst
        return wrapper
    return deco


@json_logging
@many_launch(10)
def sum_args_v1(*args, **kwargs):
    return sum(args)


if __name__ == "__main__":
    print(sum_args_v1(2, 4, 6, 8, 10, key="Hello"))
