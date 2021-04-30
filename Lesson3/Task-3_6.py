"""
    В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
    Сами минимальный и максимальный элементы в сумму не включать.
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
sum_ = 0
for el in range(SIZE):
    if array[el] > max_el:
        max_el = array[el]
        max_el_inx = el
    if array[el] < min_el:
        min_el = array[el]
        min_el_inx = el
if min_el_inx < max_el_inx:
    temp_array = array[min_el_inx + 1:max_el_inx]
    for el in range(len(temp_array)):
        sum_ = sum_ + temp_array[el]
else:
    temp_array = array[max_el_inx + 1:min_el_inx]
    for el in range(len(temp_array)):
        sum_ = sum_ + temp_array[el]

print('Минимальный и максимальный элементы массива:\n', min_el, 'и', max_el)
# print(temp_array) - вывод среза массива в качестве проверки
print('Сумма элементов, находящихся между минимальным и максимальным элементами:\n', sum_)
