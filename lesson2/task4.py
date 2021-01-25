
user_words = input('Введите несколько слов, разделённых пробелами ').split()
for number, elements in enumerate(user_words, 1):
    if len(elements) > 10:
        elements = elements[:9]
    print(f"{number}. {elements}")