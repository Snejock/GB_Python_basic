# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.

my_list = []
with open('p_05.03.txt', 'r', encoding='UTF=8') as file:
    for line in file:
        tmp = line.strip().split(' ')
        my_list.append(tmp)

print(my_list)

count = 0
sum_salary = 0
for itm in my_list:
    if int(itm[1]) < 20000:
        print(f'{itm[0]} (оклад {itm[1]})')
    count += 1
    sum_salary += int(itm[1])

print(f'Средняя заработная плата сотрудников составляет: {sum_salary/count}')
