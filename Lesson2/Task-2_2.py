""" Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
    то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)

    https://drive.google.com/file/d/10Q1r4ooc2-w_mgZgrBY4zqUlYibBHdQI/view?usp=sharing
"""


user_number = input('Введите целое положительно число:')
even_digits = 0
odd_digits = 0
for el in range(len(user_number)):
    if int(user_number[el]) % 2 == 0:
        even_digits = even_digits + 1
    else:
        odd_digits = odd_digits + 1
print(f'В чиле {user_number} четных цифр {even_digits} и нечетных цифр {odd_digits}')
