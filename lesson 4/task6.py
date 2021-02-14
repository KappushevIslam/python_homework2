from itertools import count, cycle
beginning = int(input("Введите начало диапазона "))
my_list = ["a", "b", "c", "d", "e", "f", "g", "l", "m", "n", "o", "p"]
for i in count(beginning):
    if i >= beginning + 20:
        print("двадцать итераций хватит")
        break
    else:
        print(i)





iterator = cycle(my_list)
number_of_iteration = int(input("Введите кол-во повторений списка "))
for i in range(number_of_iteration):
    print(next(iterator))
