""" Напишите программу, доказывающую или проверяющую, что для множества
    натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
    где n - любое натуральное число.

    https://drive.google.com/file/d/10Q1r4ooc2-w_mgZgrBY4zqUlYibBHdQI/view?usp=sharing
"""


def recursive_sum(digit):
    if digit == 0:
        return digit
    else:
        return digit + recursive_sum(digit - 1)


user_digit = int(input('Введите натуральное положительное число: '))
result1 = user_digit * (user_digit + 1) / 2
result2 = recursive_sum(user_digit)
if result1 == result2:
    print(f'Результат вычислений по формулам 1+2+...+n и n(n+1)/2\n'
          f'идентичны и равны: {result1, result2}')
else:
    print(f'Результат вычислений по формулам 1+2+...+n и n(n+1)/2\n'
          f'не идентичны и равны: {result1, result2}')
