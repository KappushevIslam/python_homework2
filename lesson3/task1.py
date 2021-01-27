def divide(user_number1, user_number2):
    try:
        result = round(user_number1 / user_number2, 2)
    except ZeroDivisionError:
        result = None
    return result
while True:
    user_number3 = int(input("Введите делимое "))
    user_number4 = int(input("Введите делитель "))
    if divide(user_number3, user_number4) is None:
        print("На ноль делить нельяза. Попробуйте ещё раз.")
        continue
    else:
        print(f"Результат деления: {divide(user_number3, user_number4)}")
        break
