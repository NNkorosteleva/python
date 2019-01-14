"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""
import random

a = [random.randint(-50, 50) for i in range(20)]
n = -1
for i in range(len(a)):
    if a[i] < 0 and n == -1:
        n = i
    elif a[n] < a[i] < 0:
        n = i
print(a)
print(f'Максимальный отрицательный элемент {a[n]} на позиции {n}')
