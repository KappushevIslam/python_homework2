def int_func(words):
    result = words.title()
    return result


user_answer = input("Введите ваше слова/слово ").split()
for i in user_answer:
    print(int_func(i), end=' ')
