# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

russian_dict = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре'}
src_list = []
result_dict = {}
with open('p_05.04_src.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        tmp = line.strip().split(' - ')
        src_list.append(tmp)

src_list = dict(src_list)

for value, key in src_list.items():
     result_dict[russian_dict[key]] = key

with open('p_05.04_res.txt', 'w', encoding='UTF-8') as file:
    for value, key in result_dict.items():
        file.write(f'{value} - {key}\n')
