import json
prof = 0
pr = {}
average_profit = 0
profit = {}
i = 0
with open('task7.txt', 'r') as file:
    for line in file:
        name, firm, earning, costs = line.split()
        profit[name] = int(earning) - int(costs)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        average_profit = prof / i
        print(f'Средняя прибыль равна {round(average_profit, 2)}')
    else:
        print(f'Компания работает в минус')
    pr = {'Cредняя прибыль': round(average_profit)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('task7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл json с содержимым: \n '
          f' {js_str}')
