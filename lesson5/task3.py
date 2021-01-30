# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников..
# Выполнить подсчет средней величины дохода сотрудников
with open("task3.txt", "r", encoding='utf-8') as f:
    result = 0
    for i, line in enumerate(f):
        employees, salary = line.split()
        if int(salary) < 20000:
            print(f"Зарплата работника {employees} равна {salary}")
        result += int(salary)
    print(f"Средняя величина дохода сотрудников {round(result / i, 2)}")
