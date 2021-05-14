"""
    Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых
    трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

    Условие задачи:
    Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
    Например, если введено число 3486, то надо вывести число 6843.

    https://drive.google.com/file/d/10Q1r4ooc2-w_mgZgrBY4zqUlYibBHdQI/view?usp=sharing

    Вариант №1
"""

import sys


def show(obj):
    print(f'{type(obj)=}, {sys.getsizeof(obj)=}, {obj=}')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in object.items():
                show(key)
                show(value)
            else:
                for item in obj:
                    show(item)


user_number = input('Введите целое положительно число: ')
number_len = int(len(user_number))
divider = 10
new_number = ''
for el in range(number_len):
    temp_number = str(int(user_number) % divider)
    new_number = new_number + temp_number
    user_number = str(int(user_number) // divider)
    show(temp_number)
    show(el)
print('Обратное порядку входящих цифр число:', int(new_number))

show(user_number)
show(number_len)
show(divider)
show(new_number)


"""
    Результат работы программы:
    Введите целое положительно число: 1234
    type(obj)=<class 'str'>, sys.getsizeof(obj)=50, obj='4'
    type(obj)=<class 'int'>, sys.getsizeof(obj)=24, obj=0
    type(obj)=<class 'str'>, sys.getsizeof(obj)=50, obj='3'
    type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=1
    type(obj)=<class 'str'>, sys.getsizeof(obj)=50, obj='2'
    type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=2
    type(obj)=<class 'str'>, sys.getsizeof(obj)=50, obj='1'
    type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=3
    Обратное порядку входящих цифр число: 4321
    type(obj)=<class 'str'>, sys.getsizeof(obj)=50, obj='0'
    type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=4
    type(obj)=<class 'int'>, sys.getsizeof(obj)=28, obj=10
    type(obj)=<class 'str'>, sys.getsizeof(obj)=53, obj='4321'
"""
