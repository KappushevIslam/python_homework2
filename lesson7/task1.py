# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
# Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой
# матрицы складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, list1):
        self.list1 = list1

    def __str__(self):
        return '\n'.join([' '.join(str(numb) for numb in list1) for list1 in self.list1])

    def __add__(self, other):
        new_matrix = self.list1
        for number1, value1 in enumerate(other):
            if len(new_matrix) < number1 + 1:
                new_matrix.append(other[number1])
            else:
                for number2, value2 in enumerate(value1):
                    if len(new_matrix[number1]) < number2 + 1:
                        new_matrix[number1].append(other[number1][number2])
                    else:
                        new_matrix[number1][number2] += other[number1][number2]
        return new_matrix

    def __getitem__(self, index):
        return self.list1[index]


x = Matrix([[1, 2, 3], [4, 5, 6]])
y = Matrix([[3, 2, 1], [6, 5, 4]])
print(x)
print(y)
print(x + y)
