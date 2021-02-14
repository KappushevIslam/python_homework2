def my_func1(x, y):
    return x**y


def my_func2(x, y):
    i = 1
    result = 1
    while i <= abs(y):
        result *= x
        i += 1
    return result


number_x = int(input("Введите x "))
number_y = int(input("Введите y "))
print(my_func1(number_x, number_y))
print(my_func2(number_x, number_y))