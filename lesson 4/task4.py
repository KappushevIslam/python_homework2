my_list = [1, 1, 4, 5, 5, 21, 42, 21, 7, 8, 1, 10, 7]
result_list = [numbers for numbers in my_list if my_list.count(numbers) == 1]
print(result_list)