from functools import reduce


def multiply(el_1, el_2):
    return el_1 * el_2


my_list = [numbers for numbers in range(100, 1001) if numbers % 2 ==0]
print(f"Все четные значения: {my_list}")
result = reduce(multiply, [el for el in range(99, 1001) if el % 2 == 0])
print(f"Конечный результат: {result}")