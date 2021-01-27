def my_list(number1, number2, number3):
    number_list = [number1, number2, number3]
    number_list.sort(reverse=True)
    result = number_list[0] + number_list[1]
    return result


user_answer1 = int(input("Введите первое число"))
user_answer2 = int(input("Введите второе число"))
user_answer3 = int(input("Введите третье число"))
print(f"Сумма двух наибольших чисел равна {my_list(user_answer1, user_answer2, user_answer3)}")