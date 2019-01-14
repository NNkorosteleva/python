"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы
"""
n = int(input('Число строк: '))
a = [[int(j) for j in input().split()] for i in range(n)]
for j in range(len(a[0])):
    min = a[0][j]
    for i in range(len(a)):
        if a[i][j] < min:
            min = a[i][j]
    if j == 0:
        max = min
    if min > max and j != 0:
        max = min
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max}')
