"""
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""
a = float(input('Первое число: '))
b = float(input('Второе число: '))
c = float(input('Третье число: '))
if (a > b and a < c) or (a > c and a < b):
    print(a)
elif (b > a and b < c) or (b > c and b < a):
    print(b)
else:
    print(c)