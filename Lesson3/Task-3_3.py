"""
    В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""


import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print('Массив случайных чисел:\n', array)

min_el = array[0]
max_el = array[0]
max_el_inx = 0
min_el_inx = 0
for el in range(SIZE):
    if array[el] > max_el:
        max_el = array[el]
        max_el_inx = el
    if array[el] < min_el:
        min_el = array[el]
        min_el_inx = el
print('Минимальный и максимальный элементы массива:\n', min_el, 'и', max_el)
array.pop(min_el_inx)
array.insert(min_el_inx, max_el)
array.pop(max_el_inx)
array.insert(max_el_inx, min_el)
print('Массив, в котром поменяны местами минимальный и максимальный элементы:\n', array)
