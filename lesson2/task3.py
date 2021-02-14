user_answer = int(input("Введите номер месяца "))
month_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
month_list = ['зима', 'весна', 'лето', 'осень']
if user_answer == 1 or user_answer == 12 or user_answer == 2:
    print(month_dict.get(1))
    print(month_list[0])
elif user_answer == 3 or user_answer == 4 or user_answer == 5:
    print(month_dict.get(2))
    print(month_list[1])
elif user_answer == 6 or user_answer == 7 or user_answer == 8:
    print(month_dict.get(3))
    print(month_list[2])
elif user_answer == 9 or user_answer == 10 or user_answer == 11:
    print(month_dict.get(4))
    print(month_list[3])
else:
    print("Месяца под таким номером не существует")