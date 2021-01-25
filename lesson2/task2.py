count = int(input("Введите количество элементов в списке "))
i = count
list_elements = []
while i > 0:
    ask_elements = input(f"Введите {i} элемент ")
    list_elements.append(ask_elements)
    i -= 1
print(list_elements)
i = 0
for i in range(int(len(list_elements) // 2)):
    list_elements[i], list_elements[i + 1] = list_elements[i + 1], list_elements[i]
    i += 2
print(list_elements)