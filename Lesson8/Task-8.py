"""
    Определение количества различных подстрок с использованием хэш-функции.
    Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
    Требуется найти количество различных подстрок в этой строке.
"""

string_ = input('Введите строку, состоящую из латинских букв: ').lower()
hash_list = []
for i in range(len(string_)):
    if hash(string_[i:]) not in hash_list:
        hash_list.append(hash(string_[i:]))
    for j in range(i):
        if hash(string_[j:i]) not in hash_list:
            hash_list.append(hash(string_[j:i]))
hash_list.remove(hash(string_))  # т.к. сама строка не являестя своей подстрокой
print(f'Количество различных подстрок в строке {string_} ->', len(hash_list))
