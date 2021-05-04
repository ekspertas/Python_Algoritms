"""
    Проанализировать скорость и сложность одного любого алгоритма, разработанных
    в рамках практического задания первых трех уроков.

    Задание 7 к уроку 2:
    Напишите программу, доказывающую или проверяющую, что для множества
    натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
    где n - любое натуральное число.

    https://drive.google.com/file/d/10Q1r4ooc2-w_mgZgrBY4zqUlYibBHdQI/view?usp=sharing
"""


import timeit
import cProfile


# Вариант 1
def recursive_sum(digit):
    if digit == 0:
        return digit
    else:
        return digit + recursive_sum(digit - 1)


# Вариант 2
def sum_loop(digit):
    sum_ = 0
    for el in range(digit + 1):
        sum_ = sum_ + el
    return sum_


# Вариант 3
def sum_builtins_func(digit):
    return sum([i for i in range(digit + 1)])


user_digit = int(10)
result1 = user_digit * (user_digit + 1) / 2
result2 = recursive_sum(user_digit)
if result1 == result2:
    print(f'Результат вычислений по формулам 1+2+...+n и n(n+1)/2\n'
          f'идентичны и равны: {result1, result2}')
else:
    print(f'Результат вычислений по формулам 1+2+...+n и n(n+1)/2\n'
          f'не идентичны и равны: {result1, result2}')

print('\n', timeit.timeit('recursive_sum(int(10))', number=100, globals=globals()))   # 0.00022948600000000097
print(timeit.timeit('recursive_sum(int(50))', number=100, globals=globals()))   # 0011306000000000094
print(timeit.timeit('recursive_sum(int(100))', number=100, globals=globals()))  # 002324831999999999
print(timeit.timeit('recursive_sum(int(500))', number=100, globals=globals()))  # 0.020206701999999993
print(timeit.timeit('recursive_sum(int(900))', number=100, globals=globals()))  # 0.026787499999999992
cProfile.run('recursive_sum(int(900))')
"""
         4 function calls in 0.016 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.015    0.015 <string>:1(<module>)
        1    0.015    0.015    0.015    0.015 Task-4_1.py:27(sum_loop)
        1    0.000    0.000    0.016    0.016 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

print('\n', timeit.timeit('sum_loop(int(10))', number=100, globals=globals()))   # 0.0001235700000000034
print(timeit.timeit('sum_loop(int(50))', number=100, globals=globals()))   # 0.00036578199999999506
print(timeit.timeit('sum_loop(int(100))', number=100, globals=globals()))  # 0.0007422380000000062
print(timeit.timeit('sum_loop(int(500))', number=100, globals=globals()))  # 0.0037850870000000064
print(timeit.timeit('sum_loop(int(900))', number=100, globals=globals()))  # 0.011375378999999991
cProfile.run('sum_loop(int(100000))')
"""
         4 function calls in 0.016 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.015    0.015 <string>:1(<module>)
        1    0.015    0.015    0.015    0.015 Task-4_1.py:27(sum_loop)
        1    0.000    0.000    0.016    0.016 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

print('\n', timeit.timeit('sum_builtins_func(int(10))', number=100, globals=globals()))   # 0.0003284240000000216
print(timeit.timeit('sum_builtins_func(int(50))', number=100, globals=globals()))   # 0.0006823009999999963
print(timeit.timeit('sum_builtins_func(int(100))', number=100, globals=globals()))  # 0.0012689490000000192
print(timeit.timeit('sum_builtins_func(int(500))', number=100, globals=globals()))  # 0.004713705999999984
print(timeit.timeit('sum_builtins_func(int(900))', number=100, globals=globals()))  # 0.006052035000000011
cProfile.run('sum_builtins_func(int(100000))')
"""
         6 function calls in 0.021 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.021    0.021 <string>:1(<module>)
        1    0.004    0.004    0.021    0.021 Task-4_1.py:35(sum_builtins_func)
        1    0.012    0.012    0.012    0.012 Task-4_1.py:36(<listcomp>)
        1    0.000    0.000    0.021    0.021 {built-in method builtins.exec}
        1    0.005    0.005    0.005    0.005 {built-in method builtins.sum}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

"""
В задаче финкция рвссчета суммы множества 1+2+...+n реализована тремя способами:
    Вариант 1 - используя рекурсию
    Вариант 2 - используя цикл for
    Вариант 3 - используя встроенную функцию sum
Используя функцию timeit, для измерения времени работы всех трех вариантов, видно, что быстрее всего
работает функция, где используется встроенная функция sum (на последнем месте функция с рекурсией).
Это объясняется тем, что встроенная функция написана на языке С (об этом не раз говорилось на уроках).

В тоже время, проведя анализ при помощи Профайлер, видно, что вариант функции с использованием цикла for
работает быстрее (4 function calls in 0.016 seconds), чем  вариант с встроенной функцией sum (6 function 
calls in 0.021 seconds). В моем случае, это объясняется тем, что внутри функции sum_builtins_func производистя 
формиромание списка чисел (0.012 Task-4_1.py:36(<listcomp>)), котороые только потом суммируются (0.005 {built-in method
builtins.sum}).
Что касается функции с рекурсией, то, кроме того что она медленнее всего работает, она ограничена максимальной
глубиной рекурсии в 989 повторов. Сумму более больших чисел чем 991 вычислить невозможно.
Вывод:
Если в функции передавать не целочиленное значение user_digit, а список чисел  1+2+...+user_digit, для рассчета суммы,
то, немного изменив функцию  sum_builtins_func(list(digits_list)): return sum(digits_list), можно значительно увеличить
быстродействие работы кода и, в данном случае, она будет наиболее оптимальной, для решения поставленной задачи.
"""
