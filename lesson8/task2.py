"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""


class DivisionToNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_to_null(divider, denominator):
        try:
            return divider / denominator
        except ZeroDivisionError:
            return f"Деление на ноль недопустимо"


d = DivisionToNull(10, 100)
print(DivisionToNull.divide_to_null(1, 0))
print(d.divide_to_null(1, 0))
