"""
 Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
 как коллекция, элементы которой это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’]
 и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

"""

from collections import deque

HEX_TO_DEC = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
              'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
              0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
              10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
hex_sum = deque()
tmp_var = 0

first_num = list(input('Введите 1-ое шестнадцатиричное число: ').upper())
second_num = list(input('Введите 2-ое шестнадцатиричное число: ').upper())
print('Первое число:', *first_num, '\nВторое число:',  *second_num)

if len(second_num) > len(first_num):
    first_num, second_num = deque(second_num), deque(first_num)
else:
    first_num, second_num = deque(first_num), deque(second_num)

while first_num:

    if second_num:
        result = HEX_TO_DEC[first_num.pop()] + HEX_TO_DEC[second_num.pop()] + tmp_var

    else:
        result = HEX_TO_DEC[first_num.pop()] + tmp_var

    tmp_var = 0

    if result < 16:
        hex_sum.appendleft(HEX_TO_DEC[result])

    else:
        hex_sum.appendleft(HEX_TO_DEC[result - 16])
        tmp_var = 1

if tmp_var:
    hex_sum.appendleft('1')

print('Сумма чисел равна: ', *hex_sum)
