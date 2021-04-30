"""
    В массиве найти максимальный отрицательный элемент. Вывести на экран его значение
    и позицию (индекс) в массиве.
"""


import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print('Массив случайных чисел:\n', array)

max_neg_el = array[0]
for el in range(SIZE):
    if 0 > array[el]:
        if abs(max_neg_el) > abs(array[el]):
            max_neg_el = array[el]
print('Значение максимального отрицательного эл-та массива -> ', max_neg_el,
      '\nИндекс максимального отрицательного эл-та массива -> ', array.index(max_neg_el))
