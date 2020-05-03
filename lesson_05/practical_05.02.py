# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

stroke_num = 1
words = 0
with open('p_05.02.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        words = line.strip().count(' ')+1
        print(f'Строка {stroke_num} содержит {words} слов(а)')
        stroke_num += 1

print(f'Общее число строк: {stroke_num - 1}')

