from random import randint

my_list = [randint(0, 100) for i in range(randint(5, 20))]
new_list = [el for numbers, el in enumerate(my_list) if my_list[numbers - 1] < my_list[numbers]]
print(f'Первоначальный список {my_list}')
print(f'Получившийся список {new_list}')