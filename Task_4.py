"""
Определить, какое число в массиве встречается чаще всего.
"""
import random

a = [random.randint(-50, 50) for i in range(20)]
element = a[0]
n_max = 1
for i in range(len(a)):
    n = 1
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            n += 1
    if n > n_max:
        n_max, element = n, a[i]
print(a)
if n_max > 1:
    print(f'Элемент {element} встречался {n_max} раз')
else:
    print('Все элементы уникальны')
