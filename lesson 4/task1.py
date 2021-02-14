from sys import argv
while True:
    work_hours, wage_per_hour, primium_money = argv[1:]
    try:
        wage = int(work_hours) * int(wage_per_hour) + int(primium_money)
        print(f' Зарплата равна {wage}')
    except ValueError or argv != 4:
        print("Данных не достаточно или они были введены некорректно")


 #Способ решения задачи, который мне нравится больше
def count_salary():
    while True:
        try:
            work_hours = float(input("Введите кол-ва проработанных часов "))
            wage_per_hour = float(input("Введите зарплату в час "))
            premial_money = float(input("Введите премию "))
            salary = work_hours * wage_per_hour + premial_money
            print(f"Зарплата равна {salary}")
            break
        except ValueError:
            print("Вы ввели данные некорректно")


count_salary()
