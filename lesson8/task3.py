"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
"""


class MyClass(Exception):
    def __init__(self, user_answer):
        self.user_answer = user_answer
        print(f'"{user_answer}" не число!')


my_list = []
while True:
    user_answer1 = input('Введите число или строку, для выхода нажмите q ')
    if user_answer1 != 'q':
        for number in user_answer1.split():
            try:
                if number.isdigit() is True:
                    my_list.append(int(number))
                    print(f'{number} - число!')
                else:
                    raise MyClass(number)
            except MyClass:
                pass
    else:
        break
print(f'У вас получился следущий список: {my_list}')
