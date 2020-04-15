# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1,
# 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
# необходимо использовать функцию input().

my_list = []
list_depth = 0
while list_depth <= 4:
    while True:
        print(f'Введите целое число для {list_depth} элемента списка: \n')
        itm_list = input()
        if itm_list.isdigit():
            itm_list = int(itm_list)
            my_list.append(itm_list)
            break
        else:
            print('Ошибка ввода. Введите число: \n')
    list_depth += 1

print(f'Ваш список: {my_list}')

i = 0
while i <= (len(my_list) - 2):
    tmp = my_list[i+1]
    my_list[i+1] = my_list[i]
    my_list[i] = tmp
    i += 2

print(f'Конечный список после замены: {my_list}')
