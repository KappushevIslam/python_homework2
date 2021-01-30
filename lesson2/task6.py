products = []
product_number = 1
while True:
    print("Введите данные товара")
    try:
        name = input("Введите название: ")
        price = float(input("Введите цену: "))
        quantity = int(input("Введите количество: "))
        unit = input("Введите единицу измерения: ")
    except Exception as error:
        print("Допущена ошибка ввода, пожалуйста, повторите ввод товара с самого начала!")
        continue
    products.append((product_number, {"название": name, "цена": price, "количество": quantity, "ед": unit}))
    product_number += 1
    print(products)
    analytics = {}
    for item_number, product in products:
        for product_property, product_value in product.items():
            if analytics.get(product_property) is None:
                analytics[product_property] = [product_value]
            else:
                analytics[product_property].append(product_value)
    print(analytics)