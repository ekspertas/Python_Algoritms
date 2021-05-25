"""
    Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
    на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть
    реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import random


def bubble_sort(array):
    counter = 1
    while counter < len(array):
        sort_flag = True
        for i in range(len(array) - counter):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

            sort_flag = False

        if sort_flag:
            break

        counter += 1
    return array


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99
random_array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print('Массив случайных чисел:\n', random_array)

bubble_sort(random_array)

print('Массив чисел, отсортированный в порядке убывания:\n', random_array)
