# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
# элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а
# указать явно, в программе.

my_list = [1, 2, 'str', True, 2.5, (9, 8, 7)]
for itm in my_list:
    print(type(itm))

for itm in my_list:
    if type(itm) is bool:
        print('True')
    else:
        print('False')
