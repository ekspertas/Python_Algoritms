"""
    Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
    на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы
"""

import random


def merge_sort(array, start, end):
    if end - start > 1:
        mid = (start + end)//2
        merge_sort(array, start, mid)
        merge_sort(array, mid, end)
        merge_list(array, start, mid, end)


def merge_list(array, start, mid, end):
    left = array[start:mid]
    right = array[mid:end]
    k = start
    i = 0
    j = 0
    while start + i < mid and mid + j < end:
        if left[i] <= right[j]:
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            array[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            array[k] = right[j]
            j = j + 1
            k = k + 1


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50
random_array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print('Массив случайных чисел:\n', [f'{i:.2f}' for i in random_array])

merge_sort(random_array, 0, len(random_array))
print('Массив чисел, отсортированный в порядке убывания:\n', [f'{i:.2f}' for i in random_array])
