#  Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
def counter():
    while True:
        try:
            with open('task.txt', 'w+') as f:
                line = input('Введите цифры через пробел \n')
                f.writelines(line)
                number = line.split()
                print(sum(map(int, number)))
                break
        except ValueError:
            print('Вы ввели что-то не так')


counter()
