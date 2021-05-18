"""
    Определить, какое число в массиве встречается чаще всего.
    Данные для проверки работы кода:
    SIZE = 19
    array = [56, 6, 6, 6, 6, 6, 63, 77, 77, 77, 77, 77, 77, 45, 95, 62, 0, 58, 58]
"""


import random

SIZE = 20
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print('Массив случайных чисел:\n', array)

frequent_el1 = array[0]
el_count = 1
for el in range(SIZE):
    if array.count(array[el]) > 1 and el_count < array.count(array[el]):
        frequent_el1 = array[el]
        el_count = array.count(array[el])
if el_count < 2:
    print('В массиве нет одинаковых чисел')
else:
    print('Чаще всего в массиве встречается число:\n', frequent_el1)
