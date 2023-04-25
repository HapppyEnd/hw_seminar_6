"""Задача №45. Решение в группах
Два различных натуральных числа n и m называются
дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и
наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных
чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не
превосходящее 105
. Программа должна вывести все
пары дружественных чисел, каждое из которых не
превосходит k. Пары необходимо выводить по одной в
строке, разделяя пробелами. Каждая пара должна быть
выведена только один раз (перестановка чисел новую
пару не дает).
Ввод: Вывод:
300 220 284"""

k = int(input('Введите число: '))

for res_number in range(1, k):
    sum_1 = 0
    sum_2 = 0
    for divider_1 in range(1, res_number):
        if res_number % divider_1 == 0:
            sum_1 += divider_1

    for divider_2 in range(1, sum_1):
        if sum_1 % divider_2 == 0:
            sum_2 += divider_2

    if (res_number == sum_2 and res_number != sum_1
            and res_number == min(res_number, sum_1)):
        print(res_number, sum_1)