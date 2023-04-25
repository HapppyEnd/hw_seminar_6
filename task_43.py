from random import randint
"""Задача №43. Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод:
1 2 3 2 3
Вывод: 2"""

n = int(input('введите количество элементов списка: '))

num_list = [randint(1, 10) for i in range(n)]
result_dict = {}
count = 0

for i in num_list:
    result_dict[i] = result_dict.get(i, 0) + 1

for num in result_dict.values():
    if num > 1:
        count += 1
    if num > 2 and num % 2 == 0:
        count += 1

print(f'В списке {num_list} {count} пар элементов, равных друг другу.')
