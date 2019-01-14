"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""
import random

a = [random.randint(-50, 50) for i in range(20)]
min1, min2 = a[0], a[0]
for i in a:
    if i <= min1:
        min1, min2 = i, min1
    elif min1 < i < min2:
        min2 = i
print(a)
print(f'Два наименьших элемента {min1} и {min2}')
