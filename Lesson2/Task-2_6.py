""" В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать
    не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться больше или меньше
    введенное пользователем число, чем то, что загадано. Если за 10 попыток число не отгадано, то
    вывести загаданное число.

    https://drive.google.com/file/d/10Q1r4ooc2-w_mgZgrBY4zqUlYibBHdQI/view?usp=sharing
"""

import random

random_number = random.randint(0, 100)
user_number = -1
user_try = 0
while user_try < 10 and user_number != random_number:
    user_number = int(input('Отгадайте целое число от 0 до 100: '))
    user_try = user_try + 1
    if user_number == random_number:
        print('Вы угадали!')
    else:
        if user_number > random_number:
            print('Не верно. Чилсло слишком большое. Поробуйте еще раз.')
        else:
            print('Не верно. Чилсло слишком маленькое. Поробуйте еще раз.')
if user_try == 10 and user_number != random_number:
    print('Вы не угадали за 10 попыток\nПравильный ответ:', random_number)
