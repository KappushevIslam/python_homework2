# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
translator = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
task4_2__text = []
with open("task4,1.txt", "r", encoding="utf-8") as f1:
    for i in f1:
        i = i.split(" ", 1)
        task4_2__text.append(translator[i[0]] + ' ' + i[1])
print(task4_2__text)
with open("text4,2.txt", "w", encoding="utf-8") as f2:
    f2.writelines(task4_2__text)