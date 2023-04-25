from random import randint

"""Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)"""

elements = int(input('Введите количество элементов списка: '))
list_1 = [randint(-10, 10) for i in range(elements)]

min_number = int(input('Введите первое число: '))
max_number = int(input('Введите второе число: '))

for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i, end=' ')
