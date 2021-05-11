"""
    Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
    (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
    (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и
    отдельно вывести наименования предприятий, чья прибыль ниже среднего.

"""


from collections import defaultdict


QUARTER = 4
firms = defaultdict(list)
general_avg_profit = 0

firms_count = int(input("Введите количество предприятий: "))

for i in range(firms_count):
    firm_name = input(str(i + 1) + "-ое предприятие (название): ")

    for j in range(QUARTER):
        profit = (int(input("Прибыль за " + str(j + 1) + " -й квартал: ")))
        firms[firm_name].append(profit)

    general_avg_profit = general_avg_profit + sum(firms[firm_name]) / QUARTER

general_avg_profit = general_avg_profit / firms_count
lst_of_firms = []

print('Предриятия с прибылью выше средней:')
for key in firms:
    if general_avg_profit <= sum(firms[key]) / QUARTER:
        print(key)
    else:
        lst_of_firms.append(key)

print('Предриятия с прибылью ниже средней:\n', ('\n'.join(lst_of_firms)))
