"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который
будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""


class OfficeEquipment:
    def __init__(self, name, color, index):
        self.name = name
        self.color = color
        self.index = index

    def __str__(self):
        return f'Наименование товара: {self.name}.\nЦвет: {self.color}.\nИндекс: {self.index}'


class Printer(OfficeEquipment):
    country_of_producer = "China"

    def __init__(self, *args):
        super().__init__('Принтер', *args)


class Xerox(OfficeEquipment):
    brand = 'XP'

    def __init__(self, *args):
        super().__init__('xerox', *args)


class Scanner(OfficeEquipment):
    quality = "good"

    def __init__(self, *args):
        super().__init__('scanner', *args)
