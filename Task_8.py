"""
Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""
a = int(input('Введите число: '))
n = int(input('Введите цифру, которую необходимо посчитать: '))
sum_n = 0
while a > 0:
    n_0, a = a % 10, a // 10
    if n_0 == n:
        sum_n += 1
print(f'Цифра {n} встречается {sum_n} раз')
