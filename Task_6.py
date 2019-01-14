"""
 В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
 Сами минимальный и максимальный элементы в сумму не включать.
"""
import random

a = [random.randint(-50, 50) for i in range(20)]
n_max, n_min = 0, 0
sum = 0
for i in range(len(a)):
    if a[i] > a[n_max]:
        n_max = i
    if a[i] < a[n_min]:
        n_min = i
if n_max < n_min:
    for i in range(n_max + 1, n_min):
        sum += a[i]
else:
    for i in range(n_min + 1, n_max):
        sum += a[i]
print(a)
print(f'Сумма между min и max: {sum}')
