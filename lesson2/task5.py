my_list = [2, 5, 3, 6, 7, 8]
print(sorted(my_list, reverse=True))
user_answer = 0
while user_answer != "q":
    user_answer = input("Введите числовой элемент списка. Для выхода введите 000 ")
    if user_answer == "000":
        print(sorted(my_list, reverse=True))
        break
    my_list.append(int(user_answer))
    print(sorted(my_list, reverse=True))
