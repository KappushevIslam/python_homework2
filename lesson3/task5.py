result = []
while True:
    numbers = input("Введите числа через пробел. Для выхода нажмите q ").split()
    try:
        for i in numbers:
            result.append(int(i))
        print(f"Результат сложения: {sum(result)}")
    except ValueError:
        print("Вы остановили программу ")
        break
