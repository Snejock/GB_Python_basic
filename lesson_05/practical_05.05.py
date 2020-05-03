# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

num_array = [1, 1, 2, 3, 4, 7, 11, 18, 29, 37]

with open('p_05.05.txt', 'w', encoding='UTF-8') as file:
    for itm in num_array:
        file.write(f'{itm} ')

with open('p_05.05.txt', 'r', encoding='UTF-8') as file:
    tmp_array = file.read()
    tmp_array = tmp_array.strip().split(' ')

sum_nums = 0
for itm in tmp_array:
    sum_nums += int(itm)

print(sum_nums)
