# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Clothes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_coat(self):
        result1 = round(self.width / 6.5 + 0.5, 2)
        return result1

    def calc_jacket(self):
        result2 = round(self.height * 2 + 0.3, 2)
        return result2

    @property
    def calc_sum_of_clothes(self):
        return str(f'Общая площадь ткани: {round(self.width / 6.5 + 0.5 + self.height * 2 + 0.3, 2)}')


class Coat(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.coat1 = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь ткани пальто {self.coat1}'


class Jacket(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.jacket1 = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь ткани костюма {self.jacket1}'


coat = Coat(10, 15)
jacket = Jacket(5, 10)
print(coat)
print(jacket)
print(coat.calc_sum_of_clothes)
print(jacket.calc_sum_of_clothes)

