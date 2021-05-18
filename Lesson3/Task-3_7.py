"""
    В одномерном массиве целых чисел определить два наименьших элемента.
    Они могут быть как равны между собой (оба являться минимальными), так и различаться
"""


import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print('Массив случайных чисел:\n', array)

min_el1 = array[0]
min_el2 = array[0]
for el in range(SIZE):
    if array[el] < min_el1:
        min_el1 = array[el]
for el in range(SIZE):
    if (array[el] < min_el2) and (array[el] != min_el1):
        min_el2 = array[el]
if array.count(min_el1) > 1:
    min_el2 = min_el1
print('Минимальные элементы массива:\n', min_el1, 'и', min_el2)
