# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив
# чисел, соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения
# задания обязательно использовать генератор.

my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

res_list = [itm for itm in my_list if my_list.count(itm) == 1]

print(res_list)
