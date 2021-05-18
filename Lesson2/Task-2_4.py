""" Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
    Количество элементов (n) вводится с клавиатуры.

    https://drive.google.com/file/d/10Q1r4ooc2-w_mgZgrBY4zqUlYibBHdQI/view?usp=sharing
"""


numbers_count = int(input('Введите кол-во чисел в последовательности 1 -0.5 0.25 -0.125 ...: '))
number = 1
numbers_sum = 0
for el in range(numbers_count):
    numbers_sum = numbers_sum + number
    number = number / -2
print('Сумма чисел последовательности: ', numbers_sum)
