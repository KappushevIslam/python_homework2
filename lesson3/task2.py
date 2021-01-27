def data(*args):
    return print(f"Имя: {args[0]}, фамилия: {args[1]}, год рождения: {args[2]}, город: {args[3]}, email: {args[4]}, телефон: {args[5]}")


data("Иван", "Иванов", 2000, "Москва", "vanya@mail.ru", "89123456789")