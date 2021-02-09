# 2. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны
# передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия
# всего дорожного полотна. Использовать формулу:
# длина * ширина * масса асфальта для покрытия одного кв метра дороги
# асфальтом, толщиной в 1 см * число см толщины полотна.
# Проверить работу метода.


class Road:
    def __init__(self, __length, __width):
        self.__length = __length
        self.__width = __width

    def square(self):
        return self.__length * self.__width


class road_weight(Road):
    def __init__(self, __length, __width, volume):
        super().__init__(__length, __width)
        self.volume = volume


x = road_weight(18, 50000, 12)
print(x.square())