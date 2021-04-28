""" Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
    Например, если введено число 3486, то надо вывести число 6843.

    https://drive.google.com/file/d/10Q1r4ooc2-w_mgZgrBY4zqUlYibBHdQI/view?usp=sharing
"""


user_number = input('Введите целое положительно число: ')
number_len = int(len(user_number))
divider = 10
new_number = ''
for el in range(number_len):
    temp_number = str(int(user_number) % divider)
    new_number = new_number + temp_number
    user_number = str(int(user_number) // divider)
print('Обратное порядку входящих цифр число:', int(new_number))
