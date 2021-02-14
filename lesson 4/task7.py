from random import randint
from math import factorial


def generator(list1):
    for factor in list1:
        yield factorial(factor)


my_list = list({randint(10, 30) for i in range(10)})
print(f'ЧислаБ для которых ищем факториал:: {my_list}')

a = 0
if a != len(my_list):
    for i in generator(my_list):
        print(f'Факториал {my_list[a]} равен {i}')
        a += 1
