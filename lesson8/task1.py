"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def convert_to_int(cls, date):
        result = [int(i) for i in date.split('-')]
        return result

    @staticmethod
    def validator(day, month, year):
        if day < 31:
            if month < 12:
                if year < 2021:
                    return f'Всё введено корректно!'
                else:
                    return f'Год не может быть больше 2021'
            else:
                return f'Месяц не может быть больше 12'
        else:
            return f'День не может быть больше 31'


d = Date('20 - 11 - 2020')
print(Date.convert_to_int('20-11-2020'))
print(d.validator(20, 11, 2020))