"""
 В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

a = [random.randint(-50, 50) for i in range(20)]
max, min, n_max, n_min = a[0], a[0], 0, 0
for i in range(len(a)):
    if a[i] > max:
        max, n_max = a[i], i
    if a[i] < min:
        min, n_min = a[i], i
print(f'Максимальный элекмент {max} на позиции {n_max}, Минимальный элемент {min} на позиции {n_min}')
a[n_min], a[n_max] = a[n_max], a[n_min]
print(a)
