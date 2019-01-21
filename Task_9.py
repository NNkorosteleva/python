"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр
"""
n_max, sum_max = 0, 0
print('Введите число без пробелов. Для выхода введите "!"')
while True:
    sum_n = 0
    n = input('Ввод: ')
    if n == '!':
        break
    elif n.isdigit() == True:
        n, n0 = int(n), int(n)
        while n0 > 0:
            sum_n += n0 % 10
            n0 //= 10
        if sum_n > sum_max:
            sum_max, n_max = sum_n, n
    else:
        print('Неверный ввод. Повторите попытку')
        continue
print(f'Сумма цифр числа {n_max}: {sum_max}')
